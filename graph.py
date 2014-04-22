import matplotlib
matplotlib.use('TKAgg')

from matplotlib import pyplot, animation
import numpy

figure = pyplot.figure()
ax = pyplot.axes(xlim=(0,2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = numpy.linspace(0,2, 1000)
    y = numpy.sin(2 * numpy.pi * (x - 0.01 * 1))

    line.set_data(x,y)

    return line,


anim = animation.FuncAnimation(figure, animate, init_func=init,
    frames=2000, interval=200, blit=True)


pyplot.show(block=True)



