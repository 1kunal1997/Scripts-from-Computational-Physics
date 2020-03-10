#!/usr/bin/python3

#
# Numerical Integration - Evaluate a Gaussian Integral using the rectangle approximation and the Monte Carlo approximation, and plot their fractional errors.
#
# 06June2018 - Kunal Lakhanpal
#

from pylab import *
import numpy as np
import scipy.integrate

# Function for the gaussian
def f(x):
   return np.exp(-np.power(x,2))

# Exact value of integral
AREA = scipy.integrate.quad(f,-np.inf,np.inf)[0]

# Function for rectangle approximation. Returns calculated area
# N is number of rectangles used
def rect(N):
   X = np.linspace(-50,50,N)     # Go from -50 to 50
   dx = 100 / N					# width of each rectangle
   lst = f(X) * dx				# area of each rect
   return np.sum(lst)

# Function for Monte Carlo approximation
# use a rectangle of height 1 and width 100
def monte(N):
   counter = 0
   X = np.random.random(N)*100-50    # -50 to 50
   Y = np.random.random(N)			# 0 to 1
   height = f(X)					# gaussian value for each random point
   for i,j in enumerate(Y):
      if height[i] > j:			# if random point is under the curve...
         counter += 1
   return counter / N * 100    # multiply ratio by area of rectangle (100)

#construct arrays for N values and fractional errors
N_rect = np.linspace(1,100,100)
N_monte = np.linspace(1,1000,1000)
err_rect = np.zeros_like(N_rect)
err_monte = np.zeros_like(N_monte)

# calculate error for each method
for i,j in enumerate(N_rect):
   j = int(j)
   err_rect[i] = (rect(j) - AREA) / AREA

for i,j in enumerate(N_monte):
   j = int(j)
   err_monte[i] = (monte(j) - AREA) / AREA

figure(1)

plot(N_rect,err_rect,'k-')
xlabel("Number of rectangles")
ylabel("Fractional Error")
title("Rectangle Approximation to Gaussian Integral")

figure(2)

plot(N_monte,err_monte,'k-')
xlabel("Number of Random Points")
ylabel("Fractional Error")
title("Monte Carlo Approximation to Gaussian Integral")

show()
