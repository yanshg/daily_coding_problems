#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

"""

def get_longest_increase_seq(nums,path=[]):
    if not nums:
        return path

    # float('-inf') is less than any integers
    last_val=float('-inf') if not path else path[-1]

    # exclude decreasing number
    if last_val>nums[0]:
        return get_longest_increase_seq(nums[1:],path)

    with_first=get_longest_increase_seq(nums[1:], path+[nums[0]])
    without_first=get_longest_increase_seq(nums[1:],path[:])
    #print("without_first:",without_first, "with_first:", with_first)

    # For max([iterable],key=len): if the items' length is same, then max() will return the second item
    # So put with_first as 2nd argument.
    return max([without_first,with_first], key=len)

assert get_longest_increase_seq([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])==[0,2,6,9,11,15]
