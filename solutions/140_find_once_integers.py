#!/usr/bin/python

"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

from collections import defaultdict

def get_singles(nums):
    freqs=defaultdict(int)
    for num in nums:
        freqs[num]+=1    

    return sorted([ num for num in freqs if freqs[num]==1 ])

def get_singles_with_xor(arr):
    xored = arr[0]
    for num in arr[1:]:
        xored ^= num
    x, y = 0, 0

    rightmost_set_bit = (xored & ~(xored - 1))
    for num in arr:
        if num & rightmost_set_bit:
            x ^= num
        else:
            y ^= num

    return sorted([x, y])

assert get_singles([2, 4, 6, 8, 10, 2, 6, 10])==[4, 8]
assert get_singles_with_xor([2, 4, 6, 8, 10, 2, 6, 10])==[4, 8]

