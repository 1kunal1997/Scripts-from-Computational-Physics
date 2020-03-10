#!/usr/bin/python3

#
# Gradschool Admissions - Plot the Gaussian distribution of the probabilities of getting into the grad program of three different sets of students.
#
# 02June2018 - Kunal Lakhanpal
#

from pylab import *
import numpy as np
import math

# number of students for each group
N = 787
N_g = 154
N_n = 633
# mean and standard deviation, calculated in the text file
mean = 0.186
mean_g = 0.312
mean_n = 0.155
sigma = 0.014
sigma_g = 0.037
sigma_n = 0.0144

# Gaussian function, proportional to size of group
def G(x,n,mu,sig):
   coeff = 1 / (sig*math.sqrt(2*math.pi))
   return n*coeff*np.exp(-np.power(x-mu,2) / (2*np.power(sig,2)))

# Plotting of each group of students
X = np.linspace(0,0.5,1000)
plot(X,G(X,N,mean,sigma),'k-',label='Original Population')
plot(X,G(X,N_g,mean_g,sigma_g),'r-',label='Sub-Population')
plot(X,G(X,N_n,mean_n,sigma_n),'g-',label='Remaining Population')

xlabel("Admission Probability")
ylabel("Gaussian Distribution of Probabilities")
title("Physics Ph.D Admission Probabilities ")
legend(loc='upper right')
ylim([0,23500])
xlim([0,0.5])

show()


