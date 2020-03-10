#!/usr/bin/python3

#
# Monte Carlo Circle - Calculate pi using the Monte Carlo method, and plot the
# fractional error as a function of number of points used.
#
# 26May2018 - Kunal Lakhanpal
#

from pylab import *
import numpy as np
import math

# array for number of points used, and calculated area of each of these points
N = np.linspace(1,1000,1000)
area = np.zeros_like(N)

# code from part a, looped through each number
for i,j in enumerate(N):
	j = int(j)
	X = 2 * np.random.random(j)
	Y = 2 * np.random.random(j)

	xrad, yrad = 1-X, 1-Y
	rad = np.sqrt(np.power(xrad,2) + np.power(yrad,2))	

	circ = 0.0

	for k in rad:
		if k <= 1:
			circ+=1

	area[i] = 4.0 * circ/j

# fractional error of each area
error = (area-math.pi)/math.pi

# Plotting
figure(1)

plot(N,error, 'k-')
xlabel("Number of Random Points N")
ylabel("Fractional Error of Pi")
title("Monte Carlo Method Error")

show()
