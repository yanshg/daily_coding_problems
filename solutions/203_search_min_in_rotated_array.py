#!/usr/bin/python

"""

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

"""

def helper(nums,low,high):
    while low<=high:
        mid=low + (high - low)//2
        if nums[low]<nums[mid]:
            if nums[mid]>nums[high]:
                # mid is in the left ascending part
                # smallest should be in the right part
                low=mid+1
            else:
                # the array is wholely ascending
                return nums[low]
        else:
            # mid is in the right ascending part
            # smallest should be in the left part
            high=mid-1

    return nums[low]

def get_smallest(nums):
    return helper(nums,0,len(nums)-1)

assert get_smallest([5, 7, 10, 3, 4])==3
