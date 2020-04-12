#!/usr/bin/python

"""

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

"""

# Idea: Same with problem #248:   y + ( (x-y) & b )

def choose_integer(x,y,b):
    return y + ( (x-y) & b )

assert choose_integer(2,7,1)==2
assert choose_integer(2,7,0)==7
