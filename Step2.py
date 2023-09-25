import os
import shutil
import random

# Define the folder containing the MP4 files
folder_path = "videos"

# List all MP4 files in the folder
mp4_files = [file for file in os.listdir(folder_path) if file.endswith(".mp4")]

# Check if there are at least 3 MP4 files in the folder
if len(mp4_files) < 3:
    print("There are not enough MP4 files in the folder.")
else:
    # Randomly select 3 unique MP4 files
    selected_files = random.sample(mp4_files, 3)

    # Rename and move the selected files
    for i, old_file in enumerate(selected_files):
        new_name = f"video{i + 1}.mp4"
        old_path = os.path.join(folder_path, old_file)
        new_path = os.path.join(os.path.dirname(folder_path), new_name)

        # Check if the destination file already exists
        if os.path.exists(new_path):
            print(f"File {new_name} already exists in the parent directory.")
        else:
            shutil.move(old_path, new_path)
            print(f"Moved and renamed: {old_file} -> {new_name}")
