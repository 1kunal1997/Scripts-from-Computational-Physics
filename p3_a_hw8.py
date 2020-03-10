#!/usr/bin/python3

#
# Monte Carlo Circle - Prompt the user for a number of random points to plot on
# a 2 by 2 square. Find which fraction of those points lie in a circle of radius# 1 to find an approximate value of pi.
#
# 26May2018 - Kunal Lakhanpal
#

import numpy as np
import math

# Error handling
while True:
    try:
        N = int(input("Enter the number of random points you want: "))
        break
    except ValueError:
        print("That is not a valid number")

# array for x and y coordinates
X = 2 * np.random.random(N)
Y = 2 * np.random.random(N)

# calculate radius array for all points
xrad, yrad = 1-X, 1-Y
rad = np.sqrt(np.power(xrad,2) + np.power(yrad,2))

# find number of points that lie in circle
circ = 0.0
for i in rad:
	if i <= 1:
		circ+=1

# calculate area, which is pi for radius 1 circle
area = 4.0 * circ/N
print("The area of the circle, pi, is approximately %.5f" % area)
