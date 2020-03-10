#!/usr/bin/env python3

# This program will create a 3-4-5 triangle

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# image size
X = 512
Y = 320

# array for image
pvals = np.zeros((X,Y,3), dtype='uint8')

# width of the sides of the triangle and coordinates of the sides
width = 15
sideAtop = int(0.2*Y + width/2)
sideAbot = int(0.2*Y - width/2)
sideAleft = 50
sideAright = sideAleft + 205
sideBtop = sideAright-width
sideBbot = sideAright
sideBleft = sideAbot
sideBright = sideBleft + 154

# set all pixels to white
pvals[:,:,:] = 0xff

#
# Transpose and flip rows so that origin is displayed at bottom left,
# with x horizontal and y vertical.
plotarr = np.flipud(pvals.transpose(1,0,2))

f1, ax1 = plt.subplots()

picture = ax1.imshow(plotarr, interpolation='none')

#
# turn off axis labels
ax1.axis('off')

#
# draw figure
f1.show()

# to iterate through the diagonal line
xarr = np.arange(sideAleft, sideBbot)

# bottom side
pvals[sideAleft:sideAright,sideAbot:sideAtop,:] = (0,0,0xff)  # blue
# right side
pvals[sideBtop:sideBbot,sideBleft:sideBright,:] = (0,0,0xff)  # blue

#diagonal side

# create a line starting with the bottom right, using a decision function to decide which pixels are on the line. If we are on the lin, increment both x and y, otherwise we are under the line and we increment right only until we hit the line again.
x, y = sideAleft, sideAbot
for i in range(len(xarr)):
	pvals[x , y:y+width+3,:] = (0,0,0xff)	# made a column blue
	D = 4*y - 3*x -74		# decision function
	if D <= 0:
		x += 1
		y += 1
	else: x += 1
x, y = sideAleft, sideAbot

# Code to color in the corner
for i in range(30):
    pvals[x-width-8:x , y,:] = (0,0,0xff)
    D = 4*y - 3*x -74
    if D <= 0:
        x += 1
        y += 1
    else: x += 1


picture.set_data(plotarr)
ax1.draw_artist(picture)
f1.canvas.blit(ax1.bbox)

im = Image.fromarray(plotarr, 'RGB')
im.save('triangle.tif')

input("\nPress <Enter> to exit...\n")
