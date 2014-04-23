from SimpleCV import Camera
from numpy import fft
import numpy
import helpers
import matplotlib.pyplot as plt
import time
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
plt.ion() # enable interactive graphing
plt.show()

bpm = None

while True:
    img = cam.getImage()
    sampled_img = img[sample_x0:sample_x0 + SAMPLE_WIDTH, sample_y0: sample_y0 + SAMPLE_HEIGHT]
    avg_green = helpers.sample_avg_green(sampled_img)
    green_values.append(avg_green)

    # This logic is wrong for stuff :/
    if len(green_values) >= 105: # 3.5 seconds of frames
        del green_values[:helpers.NYQUIST_FREQ] #delete the first half second of frames

        fft_val = fft.rfft(green_values)
        stuff= map(lambda n: abs(n.real), fft_val)
        potential_range = stuff[helpers.LHR_INDEX:helpers.UHR_INDEX]

        #Say the highest value is the first number, since we sliced, we want to add the LHR index offset to the value (7)
        # 0 + 7 = 7
        # 7 * .1(NYQUST_FREQ / SAMPLE_SIZE) = .7
        # .7 * 60(seconds in a minute) = 40 BPM
        max_amp_index = max(zip(potential_range, range(len(potential_range))))
        index = max_amp_index[1]  + helpers.LHR_INDEX 
        bpm = (index * helpers.HZ_MAPPER * 60)

        plt.clf() #clear the figure
        plt.plot(stuff[helpers.LHR_INDEX:helpers.UHR_INDEX])
        plt.draw()


    helpers.draw_box_outline_and_show(img, bpm)
