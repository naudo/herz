from SimpleCV import Camera, DrawingLayer
# RGB
cam = Camera()
SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = SAMPLE_WIDTH
PIXEL_COUNT = SAMPLE_HEIGHT * SAMPLE_WIDTH
GREEN=1


while True:
    img = cam.getImage()
    center_point = (img.width / 2, img.height / 2)
    boxLayer = DrawingLayer((img.width, img.height))

    sample_x0 = center_point[0] - (SAMPLE_WIDTH / 2)
    sample_y0 =  center_point[1] - (SAMPLE_HEIGHT / 2)
    
    boxLayer.centeredRectangle(center_point, (SAMPLE_WIDTH, SAMPLE_HEIGHT))
    sample = img[sample_x0:sample_x0 + SAMPLE_WIDTH, sample_y0: sample_y0 +SAMPLE_HEIGHT]

    matrix = sample.getNumpy()
    total = 0


    for row in range(0, SAMPLE_WIDTH):
        for col in matrix[row]:
            total += col[GREEN]

    print total / PIXEL_COUNT

    img.addDrawingLayer(boxLayer)
    img.applyLayers()
    img.show()
