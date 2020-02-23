#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

"""

# O(N), space O(1)

# If no index that A[i]>A[i+1], return True
#
# If two or more indices that A[i]>A[i+1], return False
#
# If only one index that A[i]>A[i+1], then need check surrounding elements:
#
#   *  if i==0 or i==len(nums)-2, then return True, since we can modify A[i]=A[i+1]
#   *  Then the case become A[i-1]<A[i]>A[i+1]<A[i+2], if A[i-1]>A[i+1] or A[i]>A[i+2], return False
#   *  other cases return True since we can modify A[i]=A[i+1]


def modify_non_decreasing_arr(nums):
    n=len(nums)

    p=None
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            if p is not None:
                return False
            p=i

    return p is None or p==0 or p==n-2 or \
            nums[p-1]<=nums[p+1] or nums[p]<=nums[p+2]

assert modify_non_decreasing_arr([10, 5, 7])
assert not modify_non_decreasing_arr([10, 5, 1])
assert not modify_non_decreasing_arr([2, 5, 1])
assert not modify_non_decreasing_arr([4, 5, 3, 4, 6])



