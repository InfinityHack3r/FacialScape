import os
import zipfile
from deepface import DeepFace
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ZipUploadForm
from .models import AnalysisResults
from collections import Counter
from webptools import cwebp

def handle_uploaded_file(zip_file):
    analysis_data = {}
    total_images = 0  # Initialize total images counter
    analyzed_images = 0  # Initialize analyzed images counter
    webp_images = []  # List to store paths of webp images

    with zipfile.ZipFile(zip_file) as z:
        z.extractall(path='temp')
        for root, dirs, files in os.walk('temp'):
            for dir in dirs:
                for file in os.listdir(os.path.join(root, dir)):
                    if file.endswith(('.jpg', '.png', '.jpeg')):
                        total_images += 1  # Increment total images counter
                        img_path = os.path.join(root, dir, file)
                        try:
                            analysis = DeepFace.analyze(img_path=img_path, actions=['emotion', 'age', 'gender', 'race'], enforce_detection=False)
                            analysis_data[img_path] = analysis
                            analyzed_images += 1  # Increment analyzed images counter

                            # Convert to webp
                            output_dir = os.path.join(settings.BASE_DIR, 'static', 'media', 'photo')
                            os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
                            output_path = os.path.join(output_dir, f'{analyzed_images}.webp')  # Define output_path here
                            cwebp(input_image=img_path, output_image=output_path, option="-q 5")
                            webp_images.append(os.path.join('static', 'media', 'photo', f'{analyzed_images}.webp'))  # Append the output path to webp_images
                            success, info = cwebp(input_image=img_path, output_image=output_path, option="-q 5")
                            print(success, info)
                        except Exception as e:
                            print(f"Failed to analyze {img_path}: {e}")

    return analysis_data, total_images, analyzed_images, webp_images  # Include webp_images in the return


def upload_and_analyze(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis_results = form.save()
            analysis_data, total_images, analyzed_images, webp_images = handle_uploaded_file(analysis_results.zip_file.path)  # Updated line
            analysis_results.analysis_data = analysis_data
            analysis_results.save()
            return redirect('display_results', analysis_results.id)
    else:
        form = ZipUploadForm()
    return render(request, 'upload.html', {'form': form})

def display_results(request, analysis_results_id):
    analysis_results = AnalysisResults.objects.get(id=analysis_results_id)
    analysis_data, total_images, analyzed_images, webp_images = handle_uploaded_file(analysis_results.zip_file.path)

    total_age, male_age_sum, female_age_sum = 0, 0, 0
    male_count, female_count = 0, 0
    emotion_counter, male_emotion_counter, female_emotion_counter = Counter(), Counter(), Counter()
    race_counter, male_race_counter, female_race_counter = Counter(), Counter(), Counter()
    
    for img_path, analysis_list in analysis_data.items():
        if analysis_list and isinstance(analysis_list[0], dict):
            analysis = analysis_list[0]
            
            gender = analysis['dominant_gender']
            if gender == 'Man':
                male_count += 1
                male_age_sum += analysis['age']
                male_emotion_counter[analysis['dominant_emotion']] += 1
                male_race_counter[analysis['dominant_race']] += 1
            else:
                female_count += 1
                female_age_sum += analysis['age']
                female_emotion_counter[analysis['dominant_emotion']] += 1
                female_race_counter[analysis['dominant_race']] += 1

            total_age += analysis['age']
            emotion_counter[analysis['dominant_emotion']] += 1
            race_counter[analysis['dominant_race']] += 1
    
    context = {
        'total_images': total_images,
        'analyzed_images': analyzed_images,
        'avg_age': total_age / (male_count + female_count) if male_count + female_count else 0,
        'avg_male_age': male_age_sum / male_count if male_count else 0,
        'avg_female_age': female_age_sum / female_count if female_count else 0,
        'primary_gender': 'Male' if male_count > female_count else 'Female',
        'male_count': male_count,
        'female_count': female_count,
        'primary_emotion': emotion_counter.most_common(1)[0][0] if emotion_counter else '',
        'primary_male_emotion': male_emotion_counter.most_common(1)[0][0] if male_emotion_counter else '',
        'primary_female_emotion': female_emotion_counter.most_common(1)[0][0] if female_emotion_counter else '',
        'primary_race': race_counter.most_common(1)[0][0] if race_counter else '',
        'primary_male_race': male_race_counter.most_common(1)[0][0] if male_race_counter else '',
        'primary_female_race': female_race_counter.most_common(1)[0][0] if female_race_counter else '',
        'analysis_data': analysis_data,
        'webp_images': webp_images,
    }
    
    return render(request, 'results.html', context)