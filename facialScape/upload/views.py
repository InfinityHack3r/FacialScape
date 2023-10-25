import os
import zipfile
import shutil
from deepface import DeepFace
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ZipUploadForm
from .models import AnalysisResults
from collections import Counter
from webptools import cwebp
from PIL import Image 
import plotly.express as px
import plotly.io as pio

def handle_uploaded_file(zip_file):
    analysis_data = {}
    total_images = 0
    analyzed_images = 0
    webp_images = []

    with zipfile.ZipFile(zip_file) as z:
        z.extractall(path='temp')  

        for root, dirs, files in os.walk('temp'):
            for dir in dirs:
                for file in os.listdir(os.path.join(root, dir)):
                    if file.endswith(('.jpg', '.png', '.jpeg')):
                        total_images += 1
                        img_path = os.path.join(root, dir, file)
                        try:
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
                            analyzed_images += 1
                        except Exception as e:
                            print(f"Failed to analyze {img_path}: {e}")

    shutil.rmtree('temp')  # Cleans up 'temp' directory after processing


    return analysis_data, total_images, analyzed_images, webp_images




def upload_and_analyze(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis_results = form.save()
            analysis_data, total_images, analyzed_images, webp_images = handle_uploaded_file(analysis_results.zip_file.path)
            analysis_results.analysis_data = analysis_data
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

    # Age Chart
    age_data = {'Age': [data['age']]}
    fig = px.bar(age_data, x=['Age'], y='Age', title='Age')
    charts_html['age_chart'] = pio.to_html(fig, full_html=False)

    # Gender Chart
    gender_data = {'Gender': [data['dominant_gender']]}
    fig = px.bar(gender_data, x=['Gender'], y='Gender', title='Gender')
    charts_html['gender_chart'] = pio.to_html(fig, full_html=False)

    # Emotion Chart
    emotions = data['emotion']
    fig = px.bar(x=list(emotions.keys()), y=list(emotions.values()), title='Emotions')
    charts_html['emotion_chart'] = pio.to_html(fig, full_html=False)

    # Race Chart
    races = data['race']
    fig = px.bar(x=list(races.keys()), y=list(races.values()), title='Races')
    charts_html['race_chart'] = pio.to_html(fig, full_html=False)

    return charts_html

def display_results(request, analysis_results_id):
    analysis_results = AnalysisResults.objects.get(id=analysis_results_id)
    analysis_data, total_images, analyzed_images, webp_images = handle_uploaded_file(analysis_results.zip_file.path)

    total_age, male_age_sum, female_age_sum = 0, 0, 0
    male_count, female_count = 0, 0
    emotion_counter, male_emotion_counter, female_emotion_counter = Counter(), Counter(), Counter()
    race_counter, male_race_counter, female_race_counter = Counter(), Counter(), Counter()
    
    avg_age_by_gender, gender_counts, emotion_counts, race_counts = prepare_chart_data(analysis_data)

    fig_age = px.bar( x=list(avg_age_by_gender.keys()),  y=list(avg_age_by_gender.values()), labels={'x': 'Gender', 'y': 'Average Age'}, title='Average Age by Gender', height=400)
    fig_age_html = pio.to_html(fig_age, full_html=False)

    fig_gender = px.pie(values=list(gender_counts.values()), names=list(gender_counts.keys()), title='Gender Distribution')
    fig_gender_html = pio.to_html(fig_gender, full_html=False)

    fig_emotion = px.bar(x=list(emotion_counts.keys()), y=list(emotion_counts.values()), title='Emotion Distribution', height=400)
    fig_emotion_html = pio.to_html(fig_emotion, full_html=False)

    fig_race = px.bar(x=list(race_counts.keys()), y=list(race_counts.values()), title='Race Distribution', height=400)
    fig_race_html = pio.to_html(fig_race, full_html=False)
    
    
    
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
    

    individual_charts_data = {}  # Dictionary to hold all charts data for each image

    for image_path, analysis_list in analysis_data.items():
        if analysis_list and isinstance(analysis_list[0], dict):
            analysis = analysis_list[0]

            # Generate the charts for this analysis
            individual_fig_age = px.bar(x=['Age'], y=[analysis['age']], title=f'Age for {image_path}', height=400)
            individual_fig_age_html = pio.to_html(individual_fig_age, full_html=False)

            individual_fig_gender = px.pie(values=[1], names=[analysis['dominant_gender']], title=f'Gender for {image_path}')
            individual_fig_gender_html = pio.to_html(individual_fig_gender, full_html=False)

            emotions = analysis['emotion']
            individual_fig_emotion = px.bar(x=list(emotions.keys()), y=list(emotions.values()), title=f'Emotions for {image_path}', height=400)
            individual_fig_emotion_html = pio.to_html(individual_fig_emotion, full_html=False)

            races = analysis['race']
            individual_fig_race = px.bar(x=list(races.keys()), y=list(races.values()), title=f'Races for {image_path}', height=400)
            individual_fig_race_html = pio.to_html(individual_fig_race, full_html=False)

            # Store the chart HTML strings in the analysis_data dictionary
            analysis_data[image_path].append({
                'fig_age_html': individual_fig_age_html,
                'fig_gender_html': individual_fig_gender_html,
                'fig_emotion_html': individual_fig_emotion_html,
                'fig_race_html': individual_fig_race_html
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
        'fig_age_html': fig_age_html,
        'fig_gender_html': fig_gender_html,
        'fig_emotion_html': fig_emotion_html,
        'fig_race_html': fig_race_html,
        'individual_fig_age_html': individual_fig_age_html,
        'individual_fig_gender_html': individual_fig_gender_html,
        'individual_fig_emotion_html': individual_fig_emotion_html,
        'individual_fig_race_html': individual_fig_race_html
    }
    
    return render(request, 'results.html', context)