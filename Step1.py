import os
import random
import string
from pytube import YouTube

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
    try:
        # Remove leading and trailing whitespace from the link
        video_url = link.strip()

        # Initialize a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Generate a random filename
        new_filename = generate_random_name() + ".mp4"

        # Download the video and save it to the 'videos' folder with the random filename
        video_stream.download(output_path='videos', filename=new_filename)

        # Remove the link from the file
        with open('./assets/links.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != link.strip():
                    file.write(line)
            file.truncate()

        print(f"Downloaded and renamed video to: {new_filename}")
    except Exception as e:
        print(f"Error downloading {link.strip()}: {str(e)}")
