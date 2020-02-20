#!/usr/bin/python

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# Idea:
# 1. Create 2 arrays:
#    a. PRE[] to record the product of all prev numbers
#    b. POST[] to record the product of all post numbers
#
# 2. PRE[i] = A[0] * A[1] * ... * A[i-1] = PRE[i-1] * A[i-1], and PRE[0]=1
#
# 3. POST[i] = A[i+1] * A[i+2] * ... * A[n] = A[i+1] * POST[i+1], and POST[n]=1
#
# 4. The new output array should be:  O[i]=PRE[i] * POST[i]

def product_all_other_nums(nums):
    pre,post=[1],[1]
    n=len(nums)

    for i in range(n-1):
        pre.append(pre[-1] * nums[i])
        post.append(post[-1] * nums[-1-i])

    return [ pre[i] * post[-1-i] for i in range(n) ]

assert product_all_other_nums([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_all_other_nums([3, 2, 1]) == [2, 3, 6]
