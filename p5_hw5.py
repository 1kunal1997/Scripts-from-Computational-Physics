#!/usr/bin/python3

# This program taken in an input of the number of petals, and then writes a .ps file to disk that contains an image of a flower with that number of petals.

while True:		# make sure input is a number
	try:
		petals = int(input("Enter the number of petals: "))
		break
	except ValueError:
		print("That wasn't a valid number")

with open("petal.ps", 'w') as f:	#write to petal.ps

	f.write("""%!PS			# standard block of code
%
% petal.ps - Draw flower petal
%
% 05May16  
% draw petal scaled by xscale and yscale, rotated by angle.
%
/petal  % xscale yscale angle petal
   {
   /petalcol [ 0.8 0 0 ] def
   /ep1 [ 0 0 ] def
   /ep2 [ 0 100 ] def
   /cp1 [ 55 65 ] def
   /cp2 [ 10 95 ] def
   /ap {aload pop} def
   gsave
   petalcol ap setrgbcolor
   0 setlinewidth
   rotate  % use angle from stack
   scale   % use xscale and yscale from stack
   ep1 ap moveto
   cp1 ap cp2 ap ep2 ap curveto
   cp2 ap exch neg exch
   cp1 ap exch neg exch
   ep1 ap curveto closepath fill

   grestore
   } def

gsave
   306 500 translate\n""")
	
	angle = 360 / petals		# angle between successive petals

	# writes the code in PS for the petals
	for i in range(petals):
		f.write("1 1 " + str(angle*i) + " petal\n")
	f.write("grestore\nshowpage\n")


