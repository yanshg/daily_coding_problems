#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

"""

def modify_non_decreasing_arr(nums,modified=False):
    if not nums or len(nums)==1:
        return True

    if nums[0]<=nums[1]:
        return modify_non_decreasing_arr(nums[1:],modified)

    return False if modified else modify_non_decreasing_arr(nums[1:],True)

assert modify_non_decreasing_arr([10, 5, 7])
assert not modify_non_decreasing_arr([10, 5, 1])

