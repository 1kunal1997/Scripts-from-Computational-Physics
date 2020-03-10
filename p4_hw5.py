#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#Takes in the real and imaginary part of a complex number and checks if it is in the set
def mandelbrot(x, y):
	bound = 4
	c = x + y*1j
	z = 0
	for i in range(250):
		z = z*z + c
		if (abs(z) > bound):
			return False
	return True
		
X = 512
Y = 384

pvals = np.zeros((X,Y), dtype='uint')

xinc = 4/X		#scaling 
yinc = 2/Y

#iterate through the pixels
for j in range(Y):
	for i in range(X):
		y = (j - Y/2) * yinc  # make image centered at the origin
		x = (i - X/2) * xinc
		# one color for in the set, one for not in set
		if mandelbrot(x,y):
			pvals[i][j] = 20
		else: pvals[i][j] = 70

plotarr = np.flipud(pvals.transpose())

f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='none', cmap='jet')
ax1.axis('off')

# draw figure
f1.show()

input("\nPress <Enter> to exit...\n")

