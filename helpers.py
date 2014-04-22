import threading
import SimpleCV


SAMPLE_RATE = 30
NYQUIST_FREQ = SAMPLE_RATE / 2 #is this actually the right name for a var

# We're just going to make the assumption that folks are alive
LOWER_HEART_RATE_BPM = 40        
UPPER_HEART_RATE_BPM = 180

LHR_HZ = LOWER_HEART_RATE_BPM / 60.0
UHR_HZ = UPPER_HEART_RATE_BPM / 60.0

# HZ_MAPPER = NYQUIST_FREQ / sample_size 
HZ_MAPPER = 0.1
# Map hz to bucket index
LHR_INDEX = int(round(LHR_HZ * 10)) #.7hz
UHR_INDEX = int(round(UHR_HZ * 10)) # 3 hz

SAMPLE_WIDTH=100
SAMPLE_HEIGHT=100

PIXEL_COUNT = SAMPLE_WIDTH * SAMPLE_HEIGHT


def sample_avg_green(img):
    matrix = img.getNumpy()
    total = 0
    for row in range(0, 100):
        for col in matrix[row]:
            total += col[1] # Get the green val

    return total / PIXEL_COUNT

def draw_box_outline_and_show(img):
    boxLayer = SimpleCV.DrawingLayer((img.width, img.height))
    boxLayer.centeredRectangle((img.width/2, img.height / 2), (SAMPLE_WIDTH, SAMPLE_HEIGHT))
    img.addDrawingLayer(boxLayer)
    img.applyLayers()
    img.show()




# maybe replace this with greenlets?
# http://greenlet.readthedocs.org/en/latest/
def set_interval(f, sec):
    def func_wrapper():
        set_interval(f, sec)
        f()
    t = threading.Timer(sec, func_wrapper)
    t.start() #this will get called once
    return t
