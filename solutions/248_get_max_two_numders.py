#!/usr/bin/python

"""

This problem was asked by Nvidia.

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

"""

# Idea: if x>y, then '(x - y) >> (INT_BIT_LENGTH)' will be 0, else be 1

import sys;

INT_BYTES = sys.getsizeof(1);
CHAR_BIT = 8;

def my_min(x, y):
    return y + ((x - y) & ((x - y) >> (INT_BYTES * CHAR_BIT - 1)))

def my_max(x, y):
    return x - ((x - y) & ((x - y) >> (INT_BYTES * CHAR_BIT - 1)))

assert my_min(7,7)==7
assert my_max(7,7)==7
assert my_min(7,8)==7
assert my_max(7,8)==8
