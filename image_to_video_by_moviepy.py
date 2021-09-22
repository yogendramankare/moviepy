# convert images to video formate by moviepy
from moviepy.editor import *

clips = []
clip1 = ImageClip(r'C:\yo Codes\image\Natural.jpg').set_duration(4)
clip2 = ImageClip(r'C:\yo Codes\image\nature2.jpg').set_duration(4)
clip3 = ImageClip(r'C:\yo Codes\image\nature3.jpg').set_duration(4)
clip4 = ImageClip(r'C:\yo Codes\image\nature4.jpg').set_duration(4)

clips.append(clip1)
clips.append(clip2)
clips.append(clip3)
clips.append(clip4)

video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile("image to video by moviepy.mp4", fps = 24, remove_temp = True, codec = "libx264", audio_codec = "aac")