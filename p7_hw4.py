#!/usr/bin/env python3

import sys
import os
from pylab import *

# This part of the code was taken from the simple_plot code to handle errors
if len(sys.argv) != 2:
   sys.stderr.write(USAGE)
   print('', file=sys.stderr)
   exit(1)

datafile = sys.argv[1]
if not os.access(datafile, os.F_OK):
   sys.stderr.write('\nData file "%s" does not exist or cannot be read.\n'
                    % datafile)
   sys.stderr.write(USAGE)
   print('',file=sys.stderr)
   exit(1)


# This code was written by me, I used this format in a previous physics class
import numpy as np

experimentinput = loadtxt(datafile, delimiter = ' ')	# load the file
experiment = transpose(experimentinput)					# split into separate vectors
time = experiment[0]
windspeed = experiment[1]
winderr = experiment[2]

figure(1)

errorbar(time, windspeed, yerr = winderr, fmt = 'ro')   # errorbar plotted
xlabel("Time t (hours)")
ylabel("Wind Speed (knots)")
title("Average Wind Speed vs. Time of Day")


show()

input("\nPress <Enter> to exit...\n")
