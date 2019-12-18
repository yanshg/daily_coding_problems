#!/usr/bin/python

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_sum_non_adjacent_numbers(nums):
    if not nums:
        return 0

    if len(nums)<= 2:
        return max(nums)

    with_first=nums[0]+max_sum_non_adjacent_numbers(nums[2:])
    without_first=max_sum_non_adjacent_numbers(nums[1:])
    return max(with_first, without_first)

assert max_sum_non_adjacent_numbers([2, 4, 6, 2, 5]) == 13
assert max_sum_non_adjacent_numbers([5, 1, 1, 5]) == 10
