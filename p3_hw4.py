#!/usr/bin/python3

# This program checks the speed of various functions in python.
import time
t = 0		# time duration of an action

for i in range(100):				# loop through 100 times to average out and get accurate
	time1 = time.perf_counter()
	pass
	time2 = time.perf_counter()
	t += (time2 - time1)
t /= 100
print("Pass statement: " + str(t))

t = 0
a, b, c, d = 4.3, 6.1, 6, 3
for i in range(100):
    time1 = time.perf_counter()
    a + b
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Addition: " + str(t))

t = 0

for i in range(100):
    time1 = time.perf_counter()
    a * b
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Multiplication: " + str(t))

t = 0

for i in range(100):
    time1 = time.perf_counter()
    a / b
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Division: " + str(t))

t = 0
for i in range(100):
    time1 = time.perf_counter()
    c // d
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Integer division: " + str(t))

num = [0] * 100000
t = 0

for i in range(100):
    time1 = time.perf_counter()
    num.append(5)
    time2 = time.perf_counter()
    num = [0] * 100000
    t += (time2 - time1)
t /= 100
print("Appending a number to large list (time depends on size of list): " + str(t))

t = 0
def test():
	pass

for i in range(100):
    time1 = time.perf_counter()
    test()
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Call to a function that does nothing: " + str(t))

def test1():
	a + b

t = 0

for i in range(100):
    time1 = time.perf_counter()
    test1()
    time2 = time.perf_counter()
    t += (time2 - time1)
t /= 100
print("Call to a function that adds: " + str(t))

