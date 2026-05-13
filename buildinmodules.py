"""
Build in modules for the language:
    math: provides mathematical functions and constants
    random: provides functions for generating random numbers
    datetime: provides classes for manipulating dates and times
    os: provides functions for interacting with the operating system
    sys: provides access to some variables used or maintained by the interpreter
"""
#math module
import math
print(math.sqrt(16))  # Output: 4.0
#random module
import random
print(random.randint(1, 10))  # Output: a random integer between 1 and 10
random.shuffle([1, 2, 3, 4, 5])  # Output: a shuffled version of the list
#time module
import time
print(time.time())  # Output: current time in seconds since the epoch
print(time.ctime())  # Output: current time in a readable format
#datetime module
import datetime
now = datetime.datetime.now()
print(now)  # Output: current date and time
#os module
import os
print(os.getcwd())  # Output: current working directory
#sys module
import sys
print(sys.version)  # Output: Python version information

