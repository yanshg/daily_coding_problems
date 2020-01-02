#!/usr/bin/python

"""

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

"""

def helper(nums,k,subset=[]):
    if not nums and k:
        return []

    if not k:
        return subset

    with_first=helper(nums[1:],k-nums[0],subset+[nums[0]])
    if with_first:
        return with_first

    without_first=helper(nums[1:], k, subset)
    if without_first:
        return without_first

    return []

def can_partition_as_two_subsets(nums):
    #print("nums: ", nums)
    s=sum(nums)
    if s%2==1:
        return False

    k=s//2
    subset=helper(nums,k)
    #print("subset: ", subset)
    if subset:
        return True
    return False

assert can_partition_as_two_subsets([15, 5, 20, 10, 35, 15, 10])
assert not can_partition_as_two_subsets([15, 5, 20, 10, 35])
