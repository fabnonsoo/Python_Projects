# IMPORTING MODULES AND EXPLORING THE STANDARD LIBRARY IN PYHTON...
# NB: I created the "mod_1" and "find_index" modules on my own text editor before running the codes in each examples....


# EXAMPLE 1:-

import mod_1 as mm                      # Used when importing the module without function
from mod_1 import find_index, test      # Used when importing the module with function
import sys

courses = ['Math', 'OpResearch', 'Statistics', 'Machine Learning']

index = find_index(courses, 'Statistics')   # OR: index = mm.find_index(courses, 'Statistics')
print(index)
print(test)

print(sys.path)


# EXAMPLE 2:-

import sys
from mod_1 import find_index, test
sys.path.append('C:\\Users\\Nonso Onyia\\Desktop\\Py-Modules')

courses = ['Math', 'OpResearch', 'Statistics', 'Machine Learning']

index = find_index(courses, 'Statistics')
print(index)
print(test)

print(sys.path)


# EXAMPLE 3:-

import random
courses = ['Math', 'OpResearch', 'Statistics', 'Machine Learning']
random_course = random.choice(courses)

print(random_course)                    # Outputs random results at different execution....


# EXAMPLE 4:-

import math
rads = math.radians(180)

print(rads)
print(math.cos(rads))                 # cosine of 90 degrees


# EXAMPLE 5:-

import calendar
import datetime

today = datetime.date.today()
print(today)

calendar_year = calendar.isleap(2020)
print(calendar_year)


# EXAMPLE 6:-

import os

print(os.getcwd())                  # Gets the current working director...
print(os.__file__)                  # Prints out the location of a file on our file system
