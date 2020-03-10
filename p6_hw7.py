#!/usr/bin/env python3
#
# p6_hw7.py - Acquire temperature data as a warmed thermometer sits in room temperature 
#
# 16May18 - Kunal Lakhanpal / Everett Lipman (fastads.py)
#

ACQTIME = 80.0  # seconds of data acquisition

#    samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
SPS = 4
nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import time
import numpy as np
from pylab import *
from scipy.optimize import curve_fit		# module for curve fitting
#
# Adafruit libraries for the temperature reader
#
import Adafruit.MCP9808 as MCP9808

###############################################################################

indata = np.zeros(nsamples,'float')

print()
print('Initializing ADC...')
print()

# temp sensor
sensor = MCP9808()

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

sensor.begin()
t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = sensor.readTempC()
   while (time.perf_counter() - st) <= sinterval:
      time.sleep(1.0e-7)

# Store temperature data in a file
with open('p6_hw7.txt','w') as f:
    for i in indata:
        f.write(str(i)+"\n")

t = time.perf_counter() - t0

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f.' % t)
print()

# define a function for curve_fit to fit to
def func(x,a,b,c):
	return a*np.exp(-b*x) + c

# popt gives the parameters for the fit func, pcov gives covariance values
popt, pcov = curve_fit(func,xpoints,indata)

# Plot of raw data with fit
figure(1)

plot(xpoints, indata, 'b-', label = 'Data')

# Plot the fit by inputting the ideal parameters into func
plot(xpoints, func(xpoints, *popt), 'k-', label = 'Fit (time constant = %5.3f)' % popt[1])
xlabel("Time t (s)")
ylabel("Temperature T (C)")
title("Naturally Cooling a Warm Plate to Room Temperature")
legend(loc='upper right')

# Plot of raw data
figure(2)
plot(xpoints, indata, 'b-')
xlabel("Time t (s)")
ylabel("Temperature T (C)")
title("Naturally Cooling a Warm Plate to Room Temperature")

show()

