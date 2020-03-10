#!/usr/bin/python3

#
# Polynomial Fits - Prompt user for a number of random points to place on the
# x-y plane. Plot them along a linear, N-1, and N-3 fit.
#
# May 26 - Kunal Lakhanpal
#

import numpy as np
from pylab import *

# Make sure user input is valid
while True:
	try:
		N = int(input("Enter the number of random points you want: "))
		break
	except ValueError:
		print("That is not a valid number")

# x and y coordinates of random points
X = 100 * np.random.random(N)
Y = 100 * np.random.random(N)

# creates the polynomials for the 3 fits 
fit1 = np.poly1d(np.polyfit(X,Y,1))
fit2 = np.poly1d(np.polyfit(X,Y,N-3))
fit3 = np.poly1d(np.polyfit(X,Y,N-1))

# array of x points for the polynomials
xpoints = np.linspace(-5,105,1000)

figure(1)

# plots
plot(X,Y,'k.')
plot(xpoints , fit1(xpoints) , 'g-', label = 'Linear fit')
plot(xpoints , fit2(xpoints) , 'b-', label = 'N-3 fit')
plot(xpoints , fit3(xpoints) , 'r-', label = 'N-1 fit')

xlabel("X axis")
ylabel("Y axis")
title("%d Random Points and Fits" %N)
xlim([-5,105])
legend(loc='upper right')
ylim([-5,105])

show()
