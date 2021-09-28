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

#add audio in video
audio = AudioFileClip(r'C:\yo Codes\sound\soundtrack.mp3')
final_video = video_clip.set_audio(audio)

final_video.write_videofile("image to video_with_audio by moviepy.mp4", fps = 24, remove_temp = True, codec = "libx264", audio_codec = "aac")
