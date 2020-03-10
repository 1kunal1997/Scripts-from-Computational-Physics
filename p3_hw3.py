#!/usr/bin/python3

# 4/17/18
# This program will prompt the user for two strings, and then create a file and place those strings in that file.

def careful_write(outlines, filename):
   """Write a list of strings to a file, if the file doesn't yet exist.

      outlines: a list of the strings to be written
      filename: where the strings will be written
   """
   import os
   import sys
   if os.access(filename, os.F_OK):
      sys.stderr.write('\nOutput file already exists: %s\n\n' % filename)
      return

   outfile = open(filename, 'w')
   for i in outlines:
      outfile.write(i)
      outfile.write(' \n')
   print ('Your file has been created! It is named %s' % filename)
   outfile.close()

string1 = input('Enter your first string: ')
string2 = input('Enter your second string: ')
careful_write([string1, string2], 'p3_hw3.txt')

