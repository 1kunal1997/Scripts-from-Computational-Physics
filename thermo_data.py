#!/usr/bin/env python3
#
# p3_hw7.py - Plot the temperature as a function of time 
#
# 16May18  Kunal Lakhanpal / Everett Lipman (stripchart.py)
#

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import math
import Adafruit.MCP9808 as MCP9808



class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.sensor = MCP9808()		# setup temperature sensor
        self.sensor.begin()
        self.Tmax = 25			# start plotting with this range
        self.Tmin = 20
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(self.Tmin, self.Tmax)
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.set_ylim(self.Tmin,self.Tmax)	# update y axis limits
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self):
        self.t0 = time.perf_counter()
        while True:
            t = time.perf_counter() - self.t0
            Tc = self.sensor.readTempC()		#read current temp

            # code for shifting the y-axis limits if temp gets larger than the max or smaller than the min
            if Tc > self.Tmax:
                self.Tmin = self.Tmin+Tc-self.Tmax + 1
                self.Tmax = Tc + 1
            if Tc < self.Tmin:
                self.Tmax = self.Tmax-Tc+self.Tmin - 1
                self.Tmin = Tc - 1

            yield t, Tc


if __name__ == '__main__':
    dt = 0.01
    fig, ax = plt.subplots()
    ax.set_ylabel("Temperature (C)")
    ax.set_xlabel("Time t (s)")
    ax.set_title("Current Temperature")
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*10., blit=True)

    plt.show()
