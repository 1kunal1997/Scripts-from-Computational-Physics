#!/usr/bin/python3

# 4/17/18
# This program will read the system's temperature in celsius and print it out once per second.

import subprocess
import time

while True:
	st = subprocess.check_output(['cat','/sys/class/thermal/thermal_zone0/temp'])
	temp = float(st) / 1000.0
	print(temp)
	time.sleep(1)  # wait for one second
	
