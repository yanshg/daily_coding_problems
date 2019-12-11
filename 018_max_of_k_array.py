#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

    Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

"""

from collections import deque

def bruteforce(nums,k):
    l=len(nums)
    return [max(nums[i:i+k]) for i in range(l-k+1)]

# use double end queue
def get_max_of_k_array(nums,k):
    results=[]

    deq=deque();
    for i in range(k):
        while deq and nums[deq[-1]] < nums[i]:
             deq.pop()
        deq.append(i)
    results.append(nums[deq[0]])

    l=len(nums)
    for i in range(k, l):
        while deq and deq[0]<=i-k:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)

        results.append(nums[deq[0]])
    return results;

assert bruteforce([10, 5, 2, 7, 8, 7],3)==[10, 7, 8, 8]
assert get_max_of_k_array([10, 5, 2, 7, 8, 7],3)==[10, 7, 8, 8]
