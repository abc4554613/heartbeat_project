from scipy import signal
from collections import deque
import serial
import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt


# [] append [[1,2,3], [4,5,6,7],[],[],[],[],[],[],[],[],[],[]] [1,2,3] [4,5,6,7]
# [] extend [1,2,3,4,5,6,7] [1,2,3] [4,5,6,7]
# Display loading


class PlotData:
    def __init__(self, max_entries=30):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = []
        self.axis_yff = deque(maxlen=max_entries)
        self.axis_yff2 = deque(maxlen=max_entries)

    def add(self, x,  y, yff, yff2):
        self.axis_x.extend(x)
        self.axis_y = y
        self.axis_yff.extend(yff)
        self.axis_yff2.extend(yff2)


# initial
fig, (ax, ax2, ax3) = plt.subplots(3, 1)
line,  = ax.plot(np.random.randn(100))
line2, = ax2.plot(np.random.randn(100))
line3, = ax3.plot(np.random.randn(100))
plt.show(block=False)
plt.setp(line2, color='r')
plt.setp(line3, color='b')


PData = PlotData(500)
ax.set_ylim(0, 1)
ax2.set_ylim(-5, 5)
ax3.set_ylim(-1, 1)


# plot parameters
print('plotting data...')
# open serial port
strPort = 'com7'
ser = serial.Serial(strPort, 115200)
ser.flush()

start = time.time()

while True:
    fs = 125
    y_value = []
    time_value = []
    y_max = []
    for ii in range(10):

        try:
            data = float(ser.readline())
            time_value.append(time.time() - start)
            y_value.append(data)

        except:
            pass
    t = np.arange(0, fs, 1/fs)
    f = np.arange(1, 125, 1)
    for i in f:
        x = np.cos(2*np.pi*i*t)
        y = signal.lfilter([1/13, 1/13, 1/13, 1/13, 1/13, 1/13,
                            1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13], 1, x)
        y_max.append(np.max(y))
    PData.add(time_value, y_max,  (y_value - np.mean(y_value)),
              signal.lfilter([1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13], 1, (y_value - np.mean(y_value))))

    ax.set_xlim(0, fs/2)
    ax2.set_xlim(PData.axis_x[0], PData.axis_x[0]+5)
    ax3.set_xlim(PData.axis_x[0], PData.axis_x[0]+5)

    line.set_xdata(f)
    line.set_ydata(PData.axis_y)
    line2.set_xdata(PData.axis_x)
    line2.set_ydata(PData.axis_yff)
    line3.set_xdata(PData.axis_x)
    line3.set_ydata(PData.axis_yff2)
    fig.canvas.draw()
    fig.canvas.flush_events()
