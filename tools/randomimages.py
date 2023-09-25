import os
import random
import shutil

def copy_random_subfolder_contents(base_folder, destination_folder, num_subfolders=1):
    # Get a list of all subfolders in the base folder
    subfolders = [d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))]
    
    # If there are no subfolders, exit
    if not subfolders:
        print("No subfolders found in the base folder.")
        return

    # Randomly select a number of subfolders without repetition
    selected_subfolders = random.sample(subfolders, min(num_subfolders, len(subfolders)))

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for random_subfolder in selected_subfolders:
        random_subfolder_path = os.path.join(base_folder, random_subfolder)

        # List all files in the randomly selected subfolder
        files = [f for f in os.listdir(random_subfolder_path) if os.path.isfile(os.path.join(random_subfolder_path, f))]

        # If there are no files, continue to the next subfolder
        if not files:
            print(f"No files found in the subfolder: {random_subfolder}")
            continue

        # Randomly select a file
        random_file = random.choice(files)
        source_file_path = os.path.join(random_subfolder_path, random_file)
        destination_file_path = os.path.join(destination_folder, random_file)

        # Copy the randomly selected file to the destination folder
        shutil.copy2(source_file_path, destination_file_path)

        print(f"Copied {random_file} from {random_subfolder} to {destination_folder}")

# Example usage
workingDir = os.getcwd()
base_folder = f"{workingDir}\DataSet\lfw-deepfunneled\lfw-deepfunneled"
destination_folder = f"{workingDir}/yoloData/randomSelect"
num_subfolders_to_copy = 100  # Change this to the desired number
copy_random_subfolder_contents(base_folder, destination_folder, num_subfolders_to_copy)
