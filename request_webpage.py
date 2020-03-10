#!/usr/bin/env python3

#
# p4_hw6.py - Get the data of the course web page using requests and print out the date of the latest update.
#
# 10May18  Kunal Lakhanpal
#

import requests

# Access the data of the web page using 'get' in requests and make it a string
req = requests.get('http://web.physics.ucsb.edu/~phys129/lipman/')
data = req.text

# Make a list of all the lines in the string block
lines = data.split('\n')
# Iterate through and find the line containing the date
for i in lines:
   if "Latest" in i:
      updateline = i
# Find the date in this line and set it to variable 'date'
firsthalf = updateline.split('">')[1]
date = firsthalf.split('<')[0]

print("Date last updated: " + date)


