#!/usr/bin/python3

import math

while True:
	x = input("Enter an angle in degrees: ")
	terms = input("Enter the number of terms: ")

	# Make sure the user entered things properly
	try:
		angle = float(x)
		terms = int(terms)
		break
	except ValueError:
		print("Enter it properly!")

# Convert to radians
angle = math.radians(angle)

approx = 0

def sind():
	global approx
	for n in range(terms):		# Series calculation of sine (formula retrieved from online)
		approx += (-1)**n * angle ** (2*n+1) / math.factorial(2*n+1)
sind()
actual = math.sin(angle)

print("Ratio of approximation and answer: " + str(approx / actual))
print("Absolute difference: " + str(abs(approx - actual)))
