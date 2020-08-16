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
    return 1 if n == 0 else (math.floor(math.log10(n)) + 1)

assert get_digits(0) == 1
assert get_digits(99) == 2
assert get_digits(100) == 3
assert get_digits(1000) == 4
assert get_digits(34576) == 5
