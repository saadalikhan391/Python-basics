#importing module calc.py
import calc
#module math   *
# from math import sqrt, factorial
# from math import *
import sys

#rename python module
# import math as mt

print(calc.add(10,2))
print(calc.substract(20,5))
# print(sqrt(25))
# print(factorial(6))
#importing sys.path
print(sys.path)

# print(mt.sqrt(16))
# print(mt.factorial(4))            # 1*2*3*4
#function to prepare th dough
def prepare_dough():
    print("preparing th dough....")

#Function to add topping
def add_toppings():
    print("Adding toppings....")

#function to bake the pizza
def bake_pizza():
    print("Baking the pizza.......")

#call the functions
prepare_dough()
add_toppings()
bake_pizza()

#Module 
#Modules are the files containing python code that can be imported into other programs.

import math

print(math.sqrt(25))

#using the pi function contained in math module 
print(math.pi)

# 2 radian = 114.59 degrees
print(math.degrees(2))

#60 degrees = 1.04 radians
print(math.radians(60))

#sine of 2 radians
print(math.sin(2))

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))

#importing module 

import random 

#printing integer between 0 to 5
print(random.randint(0,5))

#print andom floating point number between o to 1
print(random.random())

#andom number between 0 to 100
print(random.random() * 100)

# a random element from a set such as list
list = [1, True, 800,"python",27, 'hello']

print(random.choice(list))

import datetime
from datetime import date
import time

print(time.time())
#
print(date.fromtimestamp(454554))

#explorer more module 

#Calender
#use to handle operation related to calender

import calendar

year = 2023
month = 10

year1 = 2023
month1 = 11

print(calendar.month(year,month))
print(calendar.month(year1,month1))

#Printing calendar as html 
new_cal = calendar.HTMLCalendar(firstweekday=0)

print(new_cal.formatmonth(2022,8, withyear=True))


#getting the full calendar

year = 2021
print(calendar.calendar(year))

#check the leap year

x = calendar.leapdays(2016,2020)
y = calendar.isleap(2016)
z = calendar.isleap(2005)


print(x)
print(y)
print(z)


import pandas as pd

import emoji

# print(emojize(":thumnbs_up"))

print(emoji.emojize("{thumbs_up}", delimiters=("{","}")))

print(emoji.emojize("Python is fun :thumbsup:", language='alias'))
# Python is fun 👍
print(emoji.emojize("Python is fun :thumbs_up:"))
# Python is fun 👍
print(emoji.emojize("Python is fun {thumbs_up}", delimiters = ("{", "}")))
# Python is fun 👍
print(emoji.emojize("Python is fun :red_heart:", variant="text_type"))
# Python is fun ❤
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#Python is fun ❤️ # red heart, not black heart

print(emoji.emojize("this is my first emoji :thumbsup:",language='alias'))


