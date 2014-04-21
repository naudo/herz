import threading

# maybe replace this with greenlets?
# http://greenlet.readthedocs.org/en/latest/
def set_interval(f, sec):
    def func_wrapper():
        set_interval(f, sec)
        f()
    t = threading.Timer(sec, func_wrapper)
    t.start() #this will get called once
    return t


def sample_avg_green(img):
    PIXEL_COUNT = 100 * 100
    matrix = img.getNumpy()
    total = 0
    for row in range(0, 100):
        for col in matrix[row]:
            total += col[1] # Get the green val

    return total / PIXEL_COUNT