#!/usr/bin/python

"""

This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

"""

# Solution:
#
#   1. Sort all array elements in increasing order. make sure that all divisors of an element appear before it.
#   2. Use counts[] stores size of divisible subset ending with arr[i], The minimum value of counts[i] would be 1.
#   3. For every element arr[i], find a divisor arr[j] with largest value of counts[j] and set counts[i] as counts[j] + 1.

#   For example:
#   Array:    3,  5,  7, 10, 20, 21, 25
#   Index:    0,  1,  2,  3,  4,  5,  6
#   Counts:   1,  1,  1,  2,  3,  2,  2
#   Prev:    -1, -1, -1,  1,  3,  0,  1

def largest_divisible_subset(arr):
    n=len(arr)
    counts=[1]*n
    prev=[-1]*n

    arr.sort()

    max_index=0
    for i in range(1,n):
        for j in range(i):
            if arr[i]%arr[j]==0 and counts[j]+1>counts[i]:
                counts[i]=counts[j]+1
                prev[i]=j
        if counts[i]>counts[max_index]:
            max_index=i

    subset=[]
    index=max_index
    while index!=-1:
        subset+=[ arr[index] ]
        index=prev[index]

    return list(reversed(subset))

assert largest_divisible_subset([3, 5, 7, 10, 20, 21, 25])==[5, 10, 20]
assert largest_divisible_subset([1, 3, 6, 24])==[1, 3, 6, 24]

