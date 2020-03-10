#!/usr/bin/env python3

#
# p5_hw6.py - Open a TCP port and send the time a connection is made to the port to the client.
#
# 10May18  Kunal Lakhanpal, Everett Lipman (server.py)
#
USAGE="""
usage: server.py port

       Serve data from specified port.
"""
N_ARGUMENTS = (1,2)

import sys
import os
import socket
import time

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

def bind_port(prt):
   """Create socket and bind to port prt.
   """

   host = ''  # bind to all available interfaces
 
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse port
   s.bind((host, prt))
   s.listen(1)
    
   return(s)
###############################################################################

if __name__ == '__main__':
   nargs = check_arguments()
   port = int(sys.argv[1])
   thesocket = bind_port(port)

   while True:
      connection, peer = thesocket.accept()
      print()
      print('Sending data to %s...' % repr(peer), end='')

      # retrieve the time when the connection is made in a human-readable format, and store it as a string.
      st = str(time.asctime())

	  # send the time to the client, change the string the byte representation using .encode()
      connection.sendall(st.encode()) 
      print('Done.\n')
      connection.shutdown(socket.SHUT_RDWR)
      connection.close()
