#!/usr/bin/python

"""

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""

# Solution:
#
#     Use a hash table to keep track of the last position an element was seen
#     Parse through the array and keep track of the largest distinct array seen so far
#     Each time we see an element that was seen before,
#         Update the starting index of the current longest distinct array
#         That is the index to the right of the last position the current element was seen
#         Check if this length is greater than the longest distinct array we've seen so far

def longest_distinct_subarray(arr):
    positions=dict()
    start=0
    len_so_far,longest=0,0
    for i,n in enumerate(arr):
        if n not in positions or start>positions[n]:
            len_so_far+=1
            longest=max(len_so_far,longest)
        else:
            start=positions[n]+1
            len_so_far=i-start+1
        positions[n]=i
    return longest

assert longest_distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1])==5
assert longest_distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1, 4])==5
