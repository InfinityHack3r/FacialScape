import os
import zipfile
import shutil
from deepface import DeepFace
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ZipUploadForm
from .models import AnalysisResults, ImageAnalysis
from collections import Counter
from PIL import Image 
import plotly.express as px
import plotly.io as pio
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_image_hash(img_path):
    hasher = hashlib.md5()
    with open(img_path, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def handle_uploaded_file(zip_file):
    try:
        analysis_data = {}
        total_images = 0
        analyzed_images = []
        webp_images = []

        with zipfile.ZipFile(zip_file) as z:
            z.extractall(path='temp')

            for root, dirs, files in os.walk('temp'):
                for dir in dirs:
                    for file in os.listdir(os.path.join(root, dir)):
                        if file.endswith(('.jpg', '.png', '.jpeg')):
                            total_images += 1
                            img_path = os.path.join(root, dir, file)
                            img_hash = get_image_hash(img_path)  # Get the hash of the image file
                            try:
                                existing_analysis = ImageAnalysis.objects.get(image_hash=img_hash)
                            except ImageAnalysis.DoesNotExist:
                                existing_analysis = None

                            if existing_analysis:
                                analyzed_images.append(existing_analysis)
                            else:
                                try:
                                    # Assuming you have the necessary setup for DeepFace
                                    analysis = DeepFace.analyze(img_path=img_path, actions=['emotion', 'age', 'gender', 'race'], enforce_detection=False)

                                    # Directory to store webp images
                                    output_dir = os.path.join(settings.MEDIA_ROOT, 'photo')
                                    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

                                    # Keeping the file name while converting to webp
                                    output_file_name = os.path.splitext(os.path.basename(img_path))[0] + '.webp'
                                    output_path = os.path.join(output_dir, output_file_name)

                                    with Image.open(img_path) as img:
                                        img.convert('RGB').save(output_path, 'WEBP', quality=4)

                                    webp_relative_path = os.path.join('media', 'photo', output_file_name)
                                    analysis_data[webp_relative_path] = analysis  # Store analysis with new file path
                                    new_analysis = ImageAnalysis.objects.create(
                                        image_hash=img_hash,
                                        analysis_data=analysis,
                                        webp_image_path=output_path  # Assuming output_path is the path to the webp version of the image
                                    )
                                    analyzed_images.append(new_analysis)
                                except Exception as e:
                                    print(f"Failed to analyze {img_path}: {e}")

        shutil.rmtree('temp')  # Cleans up 'temp' directory after processing

        return analysis_data, total_images, analyzed_images, webp_images

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}, 0, [], []  # Return empty values in case of an error
def upload_and_analyze(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis_results = form.save()
            analysis_data, total_images, analyzed_images_list, webp_images = handle_uploaded_file(analysis_results.zip_file.path)
            analysis_results.analysis_data = analysis_data
            analysis_results.total_images = total_images
            analysis_results.analyzed_images = len(analyzed_images_list)  # Set to the length of the list
            analysis_results.webp_images = webp_images
            analysis_results.save()
            return redirect('display_results', analysis_results.id)
    else:
        form = ZipUploadForm()
    return render(request, 'upload.html', {'form': form})



def prepare_chart_data(analysis_data):
    gender_counts = Counter()
    gender_age_sum = Counter()
    emotion_counts = Counter()
    race_counts = Counter()
    
    for img_path, analysis_list in analysis_data.items():
        if analysis_list and isinstance(analysis_list[0], dict):
            analysis = analysis_list[0]
            gender = analysis['dominant_gender']
            gender_counts[gender] += 1
            gender_age_sum[gender] += analysis['age']
            emotion_counts[analysis['dominant_emotion']] += 1
            race_counts[analysis['dominant_race']] += 1
    
    avg_age_by_gender = {gender: age_sum / count for gender, (age_sum, count) in zip(gender_age_sum.keys(), zip(gender_age_sum.values(), gender_counts.values()))}
    
    return (avg_age_by_gender, gender_counts, emotion_counts, race_counts)


def generate_charts(data):
    charts_html = {}

    # Helper function to create a base64 encoded image from a Matplotlib figure
    def create_base64_image(fig):
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        return base64.b64encode(buf.getvalue()).decode('utf-8')

    # Age Chart
    fig, ax = plt.subplots()
    ax.bar('Age', data['age'])
    ax.set_title('Age')
    charts_html['age_chart'] = create_base64_image(fig)

    # Gender Chart
    fig, ax = plt.subplots()
    ax.bar('Gender', data['dominant_gender'])
    ax.set_title('Gender')
    charts_html['gender_chart'] = create_base64_image(fig)

    # Emotion Chart
    fig, ax = plt.subplots()
    emotions = data['emotion']
    ax.bar(emotions.keys(), emotions.values())
    ax.set_title('Emotions')
    charts_html['emotion_chart'] = create_base64_image(fig)

    # Race Chart
    fig, ax = plt.subplots()
    races = data['race']
    ax.bar(races.keys(), races.values())
    ax.set_title('Races')
    charts_html['race_chart'] = create_base64_image(fig)

    return charts_html

def display_results(request, analysis_results_id):
    # Get the AnalysisResults object or return a 404 if not found
    analysis_results = get_object_or_404(AnalysisResults, id=analysis_results_id)
    
    # Unpack values from analysis_results
    analysis_data = analysis_results.analysis_data
    total_images = analysis_results.total_images
    analyzed_images = analysis_results.analyzed_images
    webp_images = analysis_results.webp_images
    
    # Prepare the chart data
    avg_age_by_gender, gender_counts, emotion_counts, race_counts = prepare_chart_data(analysis_data)
    
    # Aggregate statistics
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
    
    # Generate the charts
    charts_data = generate_charts({
        'age': total_age / (male_count + female_count) if male_count + female_count else 0,
        'dominant_gender': 'Male' if male_count > female_count else 'Female',
        'emotion': emotion_counter,
        'race': race_counter
    })
    
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
        'charts_data': charts_data,
    }
    
    return render(request, 'results.html', context)