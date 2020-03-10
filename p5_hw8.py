#!/usr/bin/env python3
#
# Threaded Stripchart - Create a thread that keeps asking the user for input while plotting it on a stripchart.
#
# 26May18 - Kunal Lakhanpal / Everett Lipman 
#

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

# the number the stripchart will plot
number = 0

# thread that asks user for a number
def thethread():
	global number
	while True:
		try: 
			number = float(input("Enter a number: "))
		except ValueError:
			print("This isnt a valid number")

class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.max = 1.1
        self.min = -0.1
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.t0 = time.perf_counter()
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(self.min, self.max)
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.set_ylim(self.min, self.max)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self):
        while True:
            t = time.perf_counter() - self.t0
            # code for shifting the y-axis limits if temp gets larger than the max or smaller than the min
            if number >= self.max:
                self.min = self.min+number-self.max + 1
                self.max = number + 1
            if number <= self.min:
                self.max = self.max-number+self.min - 1
                self.min = number - 1

            yield t, number

if __name__ == '__main__':

    # start the thread as done in example
    thr = threading.Thread(target = thethread)
    thr.start()
    dt = 0.01
    fig, ax = plt.subplots()
    ax.set_xlabel("Time t (s)")
    ax.set_ylabel("User Inputted Value")
    ax.set_title("Threaded Stripchart")
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*1000., blit=False)

    plt.show()
