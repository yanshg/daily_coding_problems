#!/usr/bin/python

"""

This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

"""

def get_smallest_unsorted_window(nums):
    l=len(nums)
    left,right=0,l-1
    min_so_far,max_so_far=float('inf'),float('-inf')
    for i in range(l):
        max_so_far=max(nums[i],max_so_far)
        if nums[i]<max_so_far:
            right=i

    for i in range(l-1,-1,-1):
        min_so_far=min(nums[i],min_so_far)
        if nums[i]>min_so_far:
            left=i
    return (left,right)

assert get_smallest_unsorted_window([3, 7, 5, 6, 9])==(1,3)
