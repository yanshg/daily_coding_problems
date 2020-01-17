#!/usr/bin/python

"""

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

"""

# Idea: 1. Reverse the array
#       2. For each number, get insert position in sorted array of checked numbers.

import bisect

def bruteforce(nums):
    return [ sum(val<num for val in nums[i+1:]) for i,num in enumerate(nums) ]

def count_smaller_elements_on_right(nums):
    results,seen=[],[]

    for num in reversed(nums):
        results.append(bisect.bisect(seen,num))
        bisect.insort(seen,num)

    return results[::-1]

assert bruteforce([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
assert count_smaller_elements_on_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
