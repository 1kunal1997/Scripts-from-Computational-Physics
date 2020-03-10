#!/usr/bin/env python3

#
# p3_hw6.py - Connect to raw socket to get the course web page using ipnumber 128.111.17.41 and print out the date of latest update
# 10May18  Kunal Lakhanpal / Everett Lipman (used client.py)
#
USAGE="""
usage: p3_hw6.py [ipnum] port
       ipnum defaults to 127.0.0.1
	   ipnum for physics web page: 128.111.17.41
"""
N_ARGUMENTS = (1,2)

import sys
import os
import socket

###############################################################################

def usage(message = ''):
   sys.stdout = sys.stderr
   if message != '':
      print()
      print(message)
   print(USAGE)

   sys.exit(1)
###############################################################################

def check_arguments():
   """Check command line arguments for proper usage.
   """
   global nargs, progname
   nargs = len(sys.argv) - 1
   progname = os.path.basename(sys.argv[0])
   flag = True
   if nargs != 0 and N_ARGUMENTS[-1] == '*':
      flag = False
   else:
      for i in N_ARGUMENTS:
         if nargs == i:
            flag = False
   if flag:
      usage()
   return(nargs)
###############################################################################

def open_connection(ipn, prt):
   """Open TCP connection to ipnum:port.
   """
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
   connect_error = s.connect_ex((ipn, prt))

   if connect_error:
      if connect_error == 111:
         usage('Connection refused.  Check address and try again.')
      else:
         usage('Error %d connecting to %s:%d' % (connect_error,ipn,prt))

   return(s)
###############################################################################

def receive_data(thesock, nbytes):
   """Attempt to receive nbytes of data from open socket thesock.
   """
   dstring = b''
   rcount = 0  # number of bytes received
   thesock.settimeout(5)
   while rcount < nbytes:
      try:
         somebytes = thesock.recv(min(nbytes - rcount, 2048))
      except socket.timeout:
         print('Connection timed out.', file = sys.stderr)
         break
      if somebytes == b'':
         print('Connection closed.', file = sys.stderr)
         break
      rcount = rcount + len(somebytes)
      dstring = dstring + somebytes
      

   return(dstring)
###############################################################################

if __name__ == '__main__':
   nargs = check_arguments()

   if nargs == 1:
      ipnum = '127.0.0.1'
      port = int(sys.argv[1])
   else:
      ipnum = sys.argv[1]
      port = int(sys.argv[2])

   print()
   print('Connecting to %s, port %d...\n' % (ipnum, port))

   thesocket = open_connection(ipnum, port)

   # sending the http command to get to the course page
   thesocket.send(b'GET /~phys129/lipman/ HTTP/1.0\r\n\r\n')

   indata = receive_data(thesocket, 4096)
   thesocket.shutdown(socket.SHUT_RDWR)
   thesocket.close()

   datastring = indata.decode()
   
   # Make a list of all the lines in the string block
   lines = datastring.split('\n')
   # Iterate through and find the line containing the date
   for i in lines:
      if "Latest" in i:
         updateline = i
   # Find the date in this line and set it to variable 'date'
   firsthalf = updateline.split('">')[1]
   date = firsthalf.split('<')[0]

   print("Date last updated: " + date)

