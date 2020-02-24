#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

"""

def sum2(nums,n,k):
    hashset=set()
    for i in range(n):
        num=nums[i]
        if k-num in hashset:
            return True
        hashset.add(num)
    return False

def sum3(nums,k):
    for i in range(2,len(nums)):
        if sum2(nums,i,k-nums[i]):
            return True
    return False

assert sum3([20, 303, 3, 4, 25], 49)
assert not sum3([20, 303, 3, 4, 25], 50)

