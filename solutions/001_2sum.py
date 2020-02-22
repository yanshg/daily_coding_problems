#!/usr/bin/python

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def sum_two(nums,k):
    hashset=set()
    for num in nums:
        if k-num in hashset:
            return True
        hashset.add(num)
    return False

assert sum_two([10, 15, 3, 7], 17)
assert not sum_two([10, 15, 3, 7], 19)
