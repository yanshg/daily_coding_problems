#!/usr/bin/python

"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

# Idea:  -----------------------------x---------------
#          |- max1 -|- max2 -|        x
#                            |--------x
#                                    |
#          |<- max_so_far  ->|     max_ending_here
#
# Only include x in max_ending_here if max_ending_here + x > x

def bruteforce(arr):
    l=len(arr)
    return max([sum(arr[i:j]) for i in range(l) for j in range(i+1,l+1)])

def get_max_subarray(arr):
    max_ending_here,max_so_far=0,0
    for x in arr:
        max_ending_here=max(x, max_ending_here+x)
        max_so_far=max(max_ending_here,max_so_far)
        #print("max_ending_here:", max_ending_here, "max_so_far: ", max_so_far)
    return max_so_far

assert bruteforce([34, -50, 42, 14, -5, 86])==137
assert get_max_subarray([34, -50, 42, 14, -5, 86])==137
