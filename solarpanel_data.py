#!/usr/bin/env python3

#
# p4_hw7.py - Take a second worth of data from a solar panel and plot it
#
# 16Mar18 - Kunal Lakhanpal / Everett Lipman (fastadc.py)
#

ACQTIME = 1.0  # seconds of data acquisition

#    samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
SPS = 920

#    full-scale range in mV
#    options: 256, 512, 1024, 2048, 4096, 6144.
VRANGE = 4096

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import time
import numpy as np
from pylab import *

#
# Adafruit libraries modified by Ben Laroque for Python 3 and ADS1015
#
from Adafruit import ADS1x15
###############################################################################

indata = np.zeros(nsamples,'float')

print()
print('Initializing ADC...')
print()

#
# Default ADC IC is ADS1015
# Default address is 0x48 on the default I2C bus
#
adc = ADS1x15()

# First two arguments are the channels
# Third argument is the full-scale range in mV (default +/- 6144).
#    options: 256, 512, 1024, 2048, 4096, 6144.
#    Note: input should not exceed VDD + 0.3
# Fourth argument is samples per second (default 250).
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = 0.001*adc.getLastConversionResults()
   while (time.perf_counter() - st) <= sinterval:
      time.sleep(1.0e-7)

# take each voltage reading and write it to a file
with open('p4_1_hw7.txt','w') as f: 	
    for i in indata:
        f.write(str(i)+"\n")

t = time.perf_counter() - t0

adc.stopContinuousConversion()

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f.' % t)
print()

figure(1)

# Plot data and labels
plot(xpoints, indata, 'b-')
xlabel("Time t (s)")
ylabel("Voltage V")
title("Voltage Read From Solar Panel vs. Time")
show()

