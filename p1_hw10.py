#!/usr/bin/python3

#
# Capacitor Potential Relaxation - Calculates the potential function of a parallel plate capacitor using the relaxation method and plots it using color map.
# 
# 07June2018 - Kunal Lakhanpal
#

import numpy as np
import matplotlib.pyplot as plt

# Pre-defined values (lengths are fractions of grid size)
ITER=1000
GRID=200      # grid size
HEIGHT=0.02   # plate thickness
WIDTH=0.2     #plate width
GAP=0.04
V=5

# function for adding boundary conditions to array (returns array with boundary conditions added
def boundaries(arr, size):
   # find pixel values of lengths
   gap,width,height = int(GRID*GAP),int(GRID*WIDTH),int(GRID*HEIGHT)
   
   # set all values (except boundary) of an array of zeros to values of inputted array
   temp = np.zeros((size,size), dtype='float')
   temp[1:size-1,1:size-1] = arr[1:size-1,1:size-1]
   
   yval1 = int(size/2-gap/2-height)     #top edge of top plate
   xval = int(size/2-width/2)           #left edge of both plates
   yval2 = int(size/2+gap/2)            #top edge of bottom plate

   # use slicing to set plate to constant potential V
   temp[yval1:yval1+height , xval:xval+width] = V
   temp[yval2:yval2+height , xval:xval+width] = -V
   return temp

# 2-D arrays for current and next potential values
oldvalues = np.zeros((GRID,GRID), dtype='float')
newvalues = np.zeros((GRID,GRID), dtype='float')

# start with all zeros, with boundary conditions added
oldvalues = boundaries(oldvalues,GRID)

# iterate through to find next array using average values around each pixel from old array, assign this to old array, and repeat 
for i in range(ITER):
   # each element is average value of elements around it
   newvalues = ( np.roll(oldvalues,1,axis=1) + np.roll(oldvalues,-1,axis=1) +
   np.roll(oldvalues,1,axis=0) + np.roll(oldvalues,-1,axis=0) ) / 4.0
   # add boundaries
   newvalues = boundaries(newvalues,GRID)
   oldvalues = np.copy(newvalues)

# Plot using cmap
plotarr=np.flipud(newvalues)
f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr, interpolation='none', cmap='jet')
ax1.axis('off')
plt.colorbar(picture)
ax1.set_ylim([0,GRID-1])
ax1.set_xlim([0,GRID-1])
ax1.set_title("Potential of a Parallel Plate Capacitor")
f1.show()
input("\nPress <Enter> to exit\n")
