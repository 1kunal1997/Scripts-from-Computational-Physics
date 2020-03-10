#!/usr/bin/python3

#
# Coin Toss - Simulate 100 coin tosses and return the number of heads gotten. Call this simulation 1000 times and display on a histrogram along with a gaussian fit. 
#
# 26May18 - Kunal Lakhanpal
#

from pylab import *
import numpy as np
import math

# Values for calculating Gaussian
N,q,p = 100,0.5,0.5

# simulated 100 coin tosses and returns number of heads
def coin_toss(N=100):
	tosses = np.random.random_integers(0,1,N)  # gets 100 integers either 0 or 1
	tosses = tosses.tolist()     # convert to list and count 1's (heads)
	return tosses.count(1)

# values for Gaussian
mean = N * p
sigma = math.sqrt(N*p*q)

# Gaussian function 
def G(x):
	coeff = 1 / (sigma * math.sqrt(2*math.pi))
	return coeff * np.exp(-np.power(x-mean,2)/(2*np.power(sigma,2)))

# array for each call of the function
count = []
for i in range(1000):
	count.append(coin_toss())

# calculate number of bins needed for histogram
bins = max(count) - min(count)

# Plot normalized histogram and Gaussian function
figure(1)

X = np.linspace(0,100,1000)
hist(count,bins, normed=1)
plot(X, G(X), 'k-')
xlim([0,100])
xlabel("Number of Heads")
ylabel("Normalized Frequency")
title("Coin Toss Simulation vs. Expected Gaussian")

show()
