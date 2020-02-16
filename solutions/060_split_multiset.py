#!/usr/bin/python

"""

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

"""

def helper(nums,n,k,subset=[]):
    if not n:
        return bool(subset) if not k else False

    # with or without first number
    first=nums[-n]
    return helper(nums,n-1,k-first,subset+[first]) or \
           helper(nums,n-1,k,subset)

def can_partition_as_two_subsets(nums):
    s=sum(nums)
    if s%2==1:
        return False

    n=len(nums)
    return helper(nums,n,s//2,[])

assert can_partition_as_two_subsets([15, 5, 20, 10, 35, 15, 10])
assert not can_partition_as_two_subsets([15, 5, 20, 10, 35])
