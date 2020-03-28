#!/usr/bin/python

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

# O(2^n)
def max_sum_non_adjacent_numbers(nums):
    if not nums:
        return 0

    if len(nums)<= 2:
        return max(nums)

    with_first=nums[0]+max_sum_non_adjacent_numbers(nums[2:])
    without_first=max_sum_non_adjacent_numbers(nums[1:])
    return max(with_first, without_first)

# O(N)
def find_max_sum(nums):
    # incl:  max sum including previous element
    # excl:  max sum excluding previous element
    incl = 0
    excl = 0
    for i in nums:
        # Current max excluding i
        new_excl = excl if excl>incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return excl if excl>incl else incl

assert max_sum_non_adjacent_numbers([2, 4, 6, 2, 5]) == 13
assert max_sum_non_adjacent_numbers([5, 1, 1, 5]) == 10

assert find_max_sum([2, 4, 6, 2, 5]) == 13
assert find_max_sum([5, 1, 1, 5]) == 10
