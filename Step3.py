from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

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
