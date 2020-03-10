#!/usr/bin/python3

# 4/19/17
# This program reads in a file with numbers and prints out their average.

def file_readlines(filename):
   """Read text file and return the contents as a list of lines.
   """
   infile = open(filename, 'r')
   inlines = infile.readlines()
   infile.close()
   return(inlines)

st = input("Enter the name of your text file: ")
total = 0
contents = file_readlines(st)
print(contents)
for i in contents:
	total = total + float(i)
total = total / len(contents)

print("Your average is: %.2f" %total) 
