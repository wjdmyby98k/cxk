from  moviepy.editor import *

clip1 = VideoFileClip(r"out.avi")
size = (int(clip1.size[0]/40.0)*10,int(clip1.size[1]/40.0)*10)
clip2 = VideoFileClip(r"cxk.mp4").resize(size).set_position((clip1.size[0]-size[0],0))
CompositeVideoClip([clip1,clip2]).write_videofile(r'./pip.mp4')