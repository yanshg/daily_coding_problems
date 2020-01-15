#!/usr/bin/python

"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

"""

# Note:  last_index:  the idex of last item of the list.

def reach_last_helper(numbers, start_index, last_index):
    if start_index==last_index:
        return True

    hops=numbers[start_index]
    if start_index+hops>last_index:
        return False

    return reach_last_helper(numbers,start_index+hops,last_index)

def reach_last(numbers):
    return reach_last_helper(numbers, 0, len(numbers)-1)

assert reach_last([2,0,1,0])
assert not reach_last([1,1,0,1])
assert not reach_last([2,1])
