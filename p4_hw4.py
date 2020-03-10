#!/usr/bin/python3

import sys
fib = [1, 1]	# Default fibonacci numbers

# Make sure a number is entered
try:
	n = int(sys.argv[1])
except ValueError:
	print("That was not a number!")
	exit()
except IndexError:
	print("You have to give a number on the command line!")
	exit()

# Make sure output is not too big
if n > 75:
	print("That number is too big for the output!")
else:
	if n == 0:		# Exceptions
		fib = []
	if n == 1:
		fib = [1]
	if n == 2:
		pass
	else:
		for i in range(n-2):			# Add previous two numbers and append
			fib.append(fib[i] + fib[i+1])

	for i in fib:
		print(i, end = ", ")
	print()
	
