#!/usr/bin/python

"""

This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?

"""

# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

# Idea:  1. Find largest index i such that array[i − 1] < array[i]. (If no such i exists, then this is already the last permutation.)
#        2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
#        3. Swap array[j] and array[i − 1].
#        4. Reverse the suffix starting at array[i].

def next_permutation(nums):
    # First get longest descenting nums from the right end
    l=len(nums)
    i=l-1
    while i>0 and nums[i-1]>=nums[i]:
        i-=1

    if i>0:
        j,pivot=l-1,i-1
        while nums[j]<=nums[pivot]:
            j-=1
        nums[j],nums[pivot]=nums[pivot],nums[j]

    # Reverse suffix:
    # Note: nums[l-1:-1:-1] could not reverse the array, which return [].
    nums[i:]=reversed(nums[i:])

    return nums

assert next_permutation([1,2,3])==[1,3,2]
assert next_permutation([1,3,2])==[2,1,3]
assert next_permutation([3,2,1])==[1,2,3]
