import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange

plt.style.use('ggplot')
x_data = []
y_data = []

figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')


def grafica3(frame):
    # asfasdfasfaf
    # asfasfasf
    # temperatura
    x_data.append(datetime.now())
    y_data.append(randrange(0, 100))
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,


# animacion3 = FuncAnimation(figure, grafico, interval=5000)

animacion3 = FuncAnimation(figure, grafica3, interval=3000, cache_frame_data=False)


pyplot.show()
