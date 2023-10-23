from PIL import Image
import shutil
import os
import zipfile
from deepface import DeepFace
from django.conf import settings

def handle_uploaded_file(zip_file):
    analysis_data = {}
    total_images = 0
    analyzed_images = 0

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
                                img.convert('RGB').save(output_path, 'WEBP', quality=20) 

                            webp_relative_path = os.path.join('media', 'photo', output_file_name)
                            analysis_data[webp_relative_path] = analysis  # Store analysis with new file path
                            analyzed_images += 1
                        except Exception as e:
                            print(f"Failed to analyze {img_path}: {e}")

    shutil.rmtree('temp')  # Cleans up 'temp' directory after processing

    return analysis_data, total_images, analyzed_images
