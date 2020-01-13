#!/usr/bin/python

"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def sorted_square(nums):
    return sorted([ num*num for num in nums ])

assert sorted_square([-9, -2, 0, 2, 3])==[0, 4, 4, 9, 81]
