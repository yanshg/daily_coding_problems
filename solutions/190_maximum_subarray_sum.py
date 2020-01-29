#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

"""

def get_max_subarray_sum(nums):
    max_end_here,max_so_far=0,float('-inf')

    for num in nums:
        max_end_here=max(max_end_here+num,num)
        max_so_far=max(max_end_here,max_so_far)

    return max_so_far

def get_min_subarray_sum(nums):
    min_end_here,min_so_far=0,float('inf')

    for num in nums:
        min_end_here=min(min_end_here+num,num)
        min_so_far=min(min_end_here,min_so_far)

    return min_so_far

def get_max_wrap_subarray_sum(nums):
    s=sum(nums)
    return max(get_max_subarray_sum(nums), s-get_min_subarray_sum(nums))

assert get_max_wrap_subarray_sum([8, -1, 3, 4])==15
assert get_max_wrap_subarray_sum([-4, 5, 1, 0])==6
