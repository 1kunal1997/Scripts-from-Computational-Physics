#!/usr/bin/env python3

#
# Fork - Print all numbers starting from 1 every 1/2 a second, and at every multiple of 10, create a fork that calls the -l command.
# 
# 24May18 - Kunal Lakhanpal / Everett Lipman 
#

import os
import time

# variable for counter and return value of os.fork
counter = 0
retval = 1

# while loop for whether in parent fork or child fork
while retval:
	time.sleep(0.5)
	counter+=1
	print(counter)
	if (counter % 10 == 0):
		print("I am about to fork!")
		retval = os.fork()

# code that gets executed by child fork only (parent stays in while loop)
print("I am the child, about to execute ls!")
os.execv('/bin/ls' , ['/bin/ls' , '-l'])

 
