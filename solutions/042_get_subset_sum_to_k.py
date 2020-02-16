#!/usr/bin/python

"""

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

"""

def get_subset_sum_to_k(nums,k,subset=[]):
    if not nums:
        return subset if k==0 else None

    # with or without first number
    return get_subset_sum_to_k(nums[1:],k-nums[0],subset+[nums[0]]) or \
            get_subset_sum_to_k(nums[1:],k,subset)

assert get_subset_sum_to_k([12, 1, 61, 5, 9, 2], 24)==[12, 1, 9, 2]
assert get_subset_sum_to_k([12, 1, 61, 5, 9, 2], 100)==None
