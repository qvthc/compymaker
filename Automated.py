import os
import urllib.request
import sys
import string
from pytube import YouTube
import shutil
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Download yt-dlp and use it
if sys.platform.startswith('win32'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp.exe"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', './assets/yt-dlp/yt-dlp.exe')
elif sys.platform.startswith('darwin'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos', './assets/yt-dlp/yt-dlp')
elif sys.platform.startswith('linux'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux', './assets/yt-dlp/yt-dlp')

# Function to generate a random 5-letter text and return it
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(5))

# Create a 'videos' folder if it doesn't exist and use it
if not os.path.exists('videos'):
    os.makedirs('videos')

# Read links from the 'links.txt' file
with open('./assets/links.txt', 'r') as file:
    links = file.readlines()

# Iterate through the links and attempt to download each video
for link in links:
    if sys.platform.startswith('win32'):
        os.system(f'cd assets/yt-dlp && yt-dlp.exe -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" -P "../../videos/" "{link}"')
    else:
        os.system(f"./assets/yt-dlp/yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -P 'videos/' '{link}'")

print("\033[32m! DOWNLOAD COMPLETE !\033[0m")

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

print("\033[32m! SELECTION COMPLETE !\033[0m")

# List of input video file paths in the order you want to concatenate them
input_videos = ["./assets/intro.mp4", "video1.mp4", "video2.mp4", "video3.mp4"]

# Load each video clip
video_clips = [VideoFileClip(video_path) for video_path in input_videos]

# Concatenate the video clips sequentially
final_video = concatenate_videoclips(video_clips, method="compose")

# Write the concatenated video to an output file with "libx264" codec
final_video.write_videofile("output.mp4", codec="libx264", fps=30)  # Adjust the fps as needed

# Close the video clips
for clip in video_clips:
    clip.close()

os.remove("video1.mp4")
os.remove("video2.mp4")
os.remove("video3.mp4")

print("\033[32m! PROCESSING COMPLETE !\033[0m")
