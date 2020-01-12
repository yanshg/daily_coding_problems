#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


"""

# Article:  https://www.geeksforgeeks.org/longest-consecutive-subsequence/

# Idea:  1. First put all elements in set,
#        3. For each element, if (element-1) is not in the set, which means it is a starting point of a new sequence
#        3. For a new sequence, check how long for this sequence and get max one.


def longest_consecutive_items(nums):
    s=set(nums)
    max_seq=0

    for num in nums:
        if num-1 not in s:
            count,i=1,num+1
            while i in s:
                count+=1
                i+=1

                i+=1
            max_seq=max(max_seq,count)

