# pip install moviepy

import moviepy.editor
from tkinter.filedialog import *

#opening the file
video = askopenfilename()

# taking video to read
video = moviepy.editor.VideoFileClip(video)

#extracting the audio from video
audio = video.audio

#saving the audio file
audio.write_audiofile("audio7.mp3")

#done
print("Done..")
