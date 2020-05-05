#!/usr/bin/python

"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

# Idea:  XOR all numbers == x^y
#
#        x: 1 0 1 1 0 0 0 0
#        y: 0 1 1 0 0 0 0 0
#      x^y: 1 1 0 1 0 0 0 0
#                 ^
#                 |
#      right most 1 bit of x^y => 'rightmost'
#
#      x and y should have different bit at the 'rightmost' position
#
# Solution:  x = XOR all numbers which 'rightmost' bit is 0
#            y = XOR all numbers which 'rightmost' bit is 1
#
#      x&-x:    only keep the right most 1 bit.
#      x&(x-1): only set right most 1 bit to 0.

from collections import defaultdict

def get_singles(arr):
    xored = 0
    for num in arr:
        xored ^= num

    x, y = 0, 0
    rightmost = (xored & -xored)
    for num in arr:
        if num & rightmost:
            x ^= num
        else:
            y ^= num

    return sorted([x, y])

assert get_singles([2, 4, 6, 8, 10, 2, 6, 10])==[4, 8]

