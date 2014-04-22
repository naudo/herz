from SimpleCV import Camera, DrawingLayer
from numpy import fft
import numpy
from helpers import set_interval, sample_avg_green
# RGB
cam = Camera()
SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = SAMPLE_WIDTH
PIXEL_COUNT = SAMPLE_HEIGHT * SAMPLE_WIDTH
CAM_WIDTH = int(cam.getAllProperties().get('width'))
CAM_HEIGHT= int(cam.getAllProperties().get('height'))

cam_center_point = (CAM_HEIGHT / 2, CAM_HEIGHT / 2)
sample_x0 = cam_center_point[0] - (SAMPLE_WIDTH / 2)
sample_y0 =  cam_center_point[1] - (SAMPLE_HEIGHT / 2)
green_values = []
SAMPLE_RATE = 30 # same as the camera FPS

# 0.75 - 2.5hz
i = 0
while i < 300:
    i += 1
    img = cam.getImage()
    boxLayer = DrawingLayer((img.width, img.height))

    boxLayer.centeredRectangle(cam_center_point, (SAMPLE_WIDTH, SAMPLE_HEIGHT))
    sampled_img = img[sample_x0:sample_x0 + SAMPLE_WIDTH, sample_y0: sample_y0 + SAMPLE_HEIGHT]
    avg_green = sample_avg_green(sampled_img)

    print "Green Average Val: %d" % avg_green

    green_values.append(avg_green)

    img.addDrawingLayer(boxLayer)
    img.applyLayers()
    img.show()

del cam
fft_val = fft.rfft(green_values)
print fft_val
stuff= map(lambda n: abs(n.real), fft_val)
del stuff[0]    
print stuff

# freq = fft.fftfreq(fft_val.size -1 , d=1./SAMPLE_RATE)
# print freq
# # save the output to the file
# f = open('fft.txt', 'w')
# f.write(str(stuff))
# f.close

import matplotlib.pyplot as plt
plt.plot(stuff)
plt.show()


