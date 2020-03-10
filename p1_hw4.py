#!/usr/bin/python3

# This program prompts the user for an integer and then prints out the prime factors of that number.

import sys

while True:				# Check if user inputted an integer
	var = input("Please enter an integer: ")
	try:
		num = int(var)
		break;
	except ValueError:
		print("You did not enter an integer!", file=sys.stderr)

primes = []
i = 2
while i * 2 <= num:			# start from 2, save time by exiting if i*2 > num
	if num % i == 0:		# if divisible, add to list
		primes.append(i)
		num = int(num / i)
	else:					# if not, increment
		i += 1
if num != 1:				# exclude 1 from list
	primes.append(num)

print(primes)	
