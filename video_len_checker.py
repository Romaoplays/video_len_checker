import time
import os

from moviepy.editor import VideoFileClip

video_extensions = (".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".webm", ".mpg", ".mpeg", ".m4v")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
complete_files = []
final_strings = []

for i in range(len(files)):
   if files[i].lower().endswith(video_extensions):
        complete_files.append(files[i])

for i in range(len(complete_files)):
    clip = VideoFileClip(files[i])
    print(f"{files[i]} - {time.strftime('%H:%M:%S', time.gmtime(clip.duration))}")

