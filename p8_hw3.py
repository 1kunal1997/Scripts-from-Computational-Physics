#!/usr/bin/python3

# 4/21/19
# This program will read in names from a classlist file and wish a Happy Valentines Day to all of them

path = "/home/pi/phys129/coursefiles/classlist.csv"		#path name
classlist = open(path,"r")

for i in classlist.readlines():		#iterates through each line in the file
	info = i.split(",")				#creates a list of the words in the line
	print("Happy Valentine's Day, " + info[1].title() + " " + info[0].title() + "!")

classlist.close()
