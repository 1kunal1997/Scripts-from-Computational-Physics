#!/usr/bin/python3

#
# Counting Simulation - Plots a histogram of calling a photon counting simulation 1000 times, and overlaying a poisson distribution over it
#
# 02June2018 - Kunal Lakhanpal
#

from pylab import *
import numpy as np
import scipy.misc

# Values for poisson distribution
N = 1000
p = 0.002
mean = N*p

# Method that calculated number of photons detected
def photon(N=1000):
   rand = np.random.randint(0,1000,N)
   rand = rand.tolist()
   detected = rand.count(0) + rand.count(1)
   return detected

# Poisson Function, used scipys factorial that uses the Gamma function for float values
def pois(x,mu):
   return np.power(mu,x)*np.exp(-mu)/scipy.misc.factorial(x)

# Fill in trial values
trials = []
for i in range(1000):
   trials.append(photon())

# number of bins
bins = max(trials) - min(trials)

figure(1)

hist(trials, bins,normed=1, align='left',label='Data')
X = np.linspace(0,10,1000)
plot(X,pois(X,mean),'k-',label='Poisson Distribution')

xlabel("Number of Photons Detected")
ylabel("Normalized Frequency")
title("Photon Detection")
legend(loc='upper right')

show()
