#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.

"""

# Idea:  diff=abs(sum_all - 2 * sum_subset)


def helper(nums, sum_all, n, sum_subset=0, subset=[]):
    if n==0:
        return abs(sum_all-2*sum_subset)

    # with and without first
    first=nums[-n]
    return min(helper(nums, sum_all, n-1, sum_subset+first, subset+[first]),
               helper(nums, sum_all, n-1, sum_subset, subset))

def smallest_diff(nums):
    sum_all=sum(nums)
    n=len(nums)
    return helper(nums, sum_all, n, 0, [])

assert smallest_diff([5, 10, 15, 20, 25]) == 5
