#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

"""

# Idea:  A0,A1,A2,A3,A4,...,Ai-1,Ai,...
#        If Ai>(1+A0+A1+...+Ai-1), then there is gap, the latter should be the smallest integer which is not sum

def get_smallest_integer_not_sum(arr):
    result=1
    for num in arr:
        if num<=result:
            result+=num
        else:
            break
    return result

assert get_smallest_integer_not_sum([1, 2, 3, 10])==7

