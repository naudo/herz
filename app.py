# from moviepy.editor import VideoFileClip # for video processing
# from pylab import * # for mathematics/plotting

# # load the video, keep the clip between t=2s and t= 30s
# video = VideoFileClip('./mp4/limehouse_nights.mp4').subclip(2,30)


# # extract the focus lines in the different frames, stack them.
# roll_picture = vstack([frame[[156],58:478]
#                        for frame in video.iter_frames()])

# imshow( roll_picture ) # display the obtained picture

from SimpleCV import Camera
import time
cam = Camera()
while True:
    img = cam.getImage()
    img.show()
    time.sleep(0.01)