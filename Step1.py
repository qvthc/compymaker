import os
import sys
import urllib.request
import random
import string
import yt_dlp

# Download yt-dlp
if sys.platform.startswith('win32'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp.exe"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', './assets/yt-dlp/yt-dlp.exe')
elif sys.platform.startswith('darwin'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos', './assets/yt-dlp/yt-dlp')
elif sys.platform.startswith('linux'):
    if not os.path.exists("./assets/yt-dlp/yt-dlp"):
        urllib.request.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux', './assets/yt-dlp/yt-dlp')

# Function to generate a random 5-letter text
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(5))

# Create a 'videos' folder if it doesn't exist
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