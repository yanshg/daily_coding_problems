#!/usr/bin/python

"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

def get_permutations(nums):
    if len(nums)<2:
        return [nums]

    return [ [num]+perm for i,num in enumerate(nums) for perm in get_permutations(nums[:i]+nums[i+1:]) ]

assert get_permutations([])==[[]]
assert get_permutations([1])==[[1]]
assert get_permutations([1,2])==[[1,2], [2,1]]
assert get_permutations([1,2,3])==[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
