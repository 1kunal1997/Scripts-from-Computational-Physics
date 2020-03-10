#!/usr/bin/python3

# This program will prompt the user for a key and display information about people related to that key from a csv file.

import csv
contents = []		# list of dictionaries
with open('info.csv') as csvfile:
	csv_f = csv.reader(csvfile)
	for line in csv_f:
		contents.append( { "last":line[0], "first":line[1], "color":line[2], "food":line[3], "field":line[4], "physicist":line[5] } )

keys = list(contents[0].keys())		# list of the keys to be used
keys.sort()
print("List of keys: ")
for i in keys:
	print(i)

while True:			# outer loop only escaped by exiting 
	while True:		# inner loop checks to see if user inputted a valid key
		k = input("Pick one of these keys (type 'x' to exit): ")
		if k in keys or k == 'x':
			break;
		else:
			print("That is not a key!")
	if k == 'x':
		break;
	output = []		# list of strings to be printed
	for i in contents:
		output.append(str(i["last"]) + ", " + str(i["first"]) + ": " + str(i[k]))
	output.sort()		#alphabetical order
	for i in output:
		print(i)
