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

complete_files = sorted(complete_files)
total_duration = 0

for i in range(len(complete_files)):
    clip = VideoFileClip(complete_files[i])
    total_duration += clip.duration
    print(f"{complete_files[i]} - {time.strftime('%H:%M:%S', time.gmtime(clip.duration))}")


print(f"---- Total Length: {time.strftime('%H:%M:%S', time.gmtime(total_duration))} ----")
