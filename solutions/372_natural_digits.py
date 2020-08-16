#!/usr/bin/python

"""

This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.

"""

# Use log10(logarithm of base 10) to count the number of digits of positive numbers
#
# Digit count of N = upper bound of log10(N).

import math

def get_digits(n):
    return math.floor(math.log(n,10)+1)

assert get_digits(34576) == 5
