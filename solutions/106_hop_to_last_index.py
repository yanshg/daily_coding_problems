#!/usr/bin/python

"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

"""

# Note:  end:  the idex of last item of the list.

def helper(nums,start,end):
    if start==end:
        return True
    elif start>end:
        return False

    hops=nums[start]
    if hops==0:
        return False

    return helper(nums,start+nums[start],end)

def reach_end(nums):
    return helper(nums,0,len(nums)-1)

assert reach_end([2,0,1,0])
assert not reach_end([1,1,0,1])
assert not reach_end([2,1])
