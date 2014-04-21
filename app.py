from SimpleCV import Camera, DrawingLayer
from numpy import fft
from helpers import set_interval, sample_avg_green
# RGB
cam = Camera()
SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = SAMPLE_WIDTH
PIXEL_COUNT = SAMPLE_HEIGHT * SAMPLE_WIDTH
CAM_WIDTH = int(cam.getAllProperties().get('width'))
CAM_HEIGHT= int(cam.getAllProperties().get('height'))

cam_center_point = ( CAM_HEIGHT / 2, CAM_HEIGHT / 2)
sample_x0 = cam_center_point[0] - (SAMPLE_WIDTH / 2)
sample_y0 =  cam_center_point[1] - (SAMPLE_HEIGHT / 2)
green_values = []



def do_rfft():
    print fft.fft(green_values)

set_interval(do_rfft, 10) #process stuff every second

while True:
    img = cam.getImage()
    boxLayer = DrawingLayer((img.width, img.height))
    
    boxLayer.centeredRectangle(cam_center_point, (SAMPLE_WIDTH, SAMPLE_HEIGHT))
    avg_green = sample_avg_green(img[sample_x0:sample_x0 + SAMPLE_WIDTH, sample_y0: sample_y0 +SAMPLE_HEIGHT])

    
    print "Green Average Val: %d" % avg_green

    green_values.append(avg_green)

    img.addDrawingLayer(boxLayer)
    img.applyLayers()
    img.show()
