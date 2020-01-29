#!/usr/bin/python

"""

This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

"""

def helper(nums,pos=0,path_so_far=[0]):
    assert nums

    l=len(nums)
    if pos>=l:
        return False
    elif pos==l-1:
        print("path: ", path_so_far)
        return True

    for steps in range(nums[pos],0,-1):
        index=pos+steps
        if helper(nums,index,path_so_far+[index]):
            return True

    return False

def advance_array_to_end(nums):
    return helper(nums,0,[0])

assert advance_array_to_end([1, 3, 1, 2, 0, 1])
assert not advance_array_to_end([1, 2, 1, 0, 0])
