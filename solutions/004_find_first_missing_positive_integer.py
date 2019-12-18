#!/usr/bin/python

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def find_first_missing_positive_integer(arr):
    exists={ n:1 for n in arr }

    found=None

    for n in arr:
        num=n+1
        if num not in exists:
            if not found or num<found:
                found=num

    if not found or found<=0:
        found=1

    return found

assert find_first_missing_positive_integer([3, 4, -1, 1])==2
assert find_first_missing_positive_integer([1, 2, 0])==3
assert find_first_missing_positive_integer([1, 2, 5]) == 3
assert find_first_missing_positive_integer([1]) == 2
assert find_first_missing_positive_integer([-1, -2]) == 1
assert find_first_missing_positive_integer([]) == 1
