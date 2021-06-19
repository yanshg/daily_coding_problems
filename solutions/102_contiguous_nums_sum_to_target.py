#!/usr/bin/python

"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

"""

# Prefix sum
def get_contiguous_numbers_sum_to_target(list,target):
    l=len(list)
    sums=[];
    for i in range(l):
        if list[i] == target:
            return list[i:i+1]
        for j in range(len(sums)):
            s=list[i]+sums[j]
            if s==target:
                return list[j:i+1]
            sums[j]=s
        sums.append(list[i])
    return []

# if all positive integers
def get_contiguous_positive_numbers_sum_to_target(list,target):
    summed=0
    start=end=0
    while end<len(list):
        if summed==target:
            return list[start:end]
        elif summed>target:
            summed-=list[start]
            start+=1
        elif summed<target:
            summed+=list[end]
            end+=1
    return []

assert get_contiguous_numbers_sum_to_target([1, 2, 3, 4, 5], 0) == []
assert get_contiguous_numbers_sum_to_target([1, 2, 3, 4, 5], 1) == [1]
assert get_contiguous_numbers_sum_to_target([1, 2, 3, 4, 5], 5) == [2, 3]
assert get_contiguous_numbers_sum_to_target([5, 4, 3, 4, 5], 12) == [5, 4, 3]
assert get_contiguous_numbers_sum_to_target([5, 4, 3, 4, 5], 11) == [4, 3, 4]
assert get_contiguous_numbers_sum_to_target([1, 2, 3, 4, 5], 9) == [2, 3, 4]
assert get_contiguous_numbers_sum_to_target([1, 2, 3, 4, 5], 3) == [1, 2]

assert get_contiguous_positive_numbers_sum_to_target([1, 2, 3, 4, 5], 0) == []
assert get_contiguous_positive_numbers_sum_to_target([1, 2, 3, 4, 5], 1) == [1]
assert get_contiguous_positive_numbers_sum_to_target([1, 2, 3, 4, 5], 5) == [2, 3]
assert get_contiguous_positive_numbers_sum_to_target([5, 4, 3, 4, 5], 12) == [5, 4, 3]
assert get_contiguous_positive_numbers_sum_to_target([5, 4, 3, 4, 5], 11) == [4, 3, 4]
assert get_contiguous_positive_numbers_sum_to_target([1, 2, 3, 4, 5], 9) == [2, 3, 4]
assert get_contiguous_positive_numbers_sum_to_target([1, 2, 3, 4, 5], 3) == [1, 2]
