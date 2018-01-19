# Author: Alfredo Ceballos
# Assignment: Lab #2
# Completed: 1/8/2018

from math import sqrt

# Part 1

# Created a function that takes in the rate as an argument and
# finds the total of a savings account with an initial deposit
# of $1000 with a time of 18 years to compound. Output is formatted
# and the total is rounded to 2 decimal places
def calc_total(rate):
    initial_deposit = 1000
    num_years = 18
    total = initial_deposit * ((1 + (rate / 100)) ** num_years)
    print("At %d%% rate total is %.2f" % (rate, total))

calc_total(3) # Rate 0f 3%
calc_total(5) # Rate of 5%
calc_total(12)# Rate of 12%

"""
initial_deposit = 1000
rate = 3
num_years = 18
total = initial_deposit * ((1 + (rate / 100)) ** num_years)
print("At 3%% rate total is %.2f" % total)

rate = 5
total = initial_deposit * ((1 + (rate / 100)) ** num_years)
print("At 5%% rate total is %.2f" % total)

rate = 12
total = initial_deposit * ((1 + (rate / 100)) ** num_years)
print("At 12%% rate total is %.2f" % total)
"""

# Part 2

# Getting user input and saving those values as floating point numbers
# using 'a' and 'b'
a = float(input("Input a number: "))
b = float(input("Input another number: "))

# Calculating the length of the hypotenuse of a triangle with sides of
# that length
hyp = sqrt((a * a) + (b * b))

# Printing value of the hypotenuse and rounding it to 3 decimal places
print("The hypotenuse of a triangle with these sides would be %.3f" % hyp)

""" OUTPUT
At 3% rate total is 1702.43
At 5% rate total is 2406.62
At 12% rate total is 7689.97
Input a number: 32
Input another number: 12
The hypotenuse of a triangle with these sides would be 34.176
"""
