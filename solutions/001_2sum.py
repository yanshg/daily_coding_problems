#!/usr/bin/python

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def sum_two(nums,k):
    hash=dict()
    for i in nums:
        if k-i in hash:
            return True
        hash[i]=1
    return False

assert sum_two([10, 15, 3, 7], 17)
assert not sum_two([10, 15, 3, 7], 19)
