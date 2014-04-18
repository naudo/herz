from SimpleCV import Camera
# RGB
cam = Camera()
SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = SAMPLE_WIDTH
SAMPLE_OFFSET = 0
PIXEL_COUNT = SAMPLE_HEIGHT * SAMPLE_WIDTH
GREEN=1

while True:
    img = cam.getImage()
    img2 = img[SAMPLE_OFFSET:SAMPLE_WIDTH, SAMPLE_OFFSET:SAMPLE_HEIGHT]
    matrix = img2.getNumpy()
    total = 0
    for row in range(0, SAMPLE_WIDTH):
        for col in matrix[row]:
            total += col[GREEN]

    print total / PIXEL_COUNT

    img2.show()
