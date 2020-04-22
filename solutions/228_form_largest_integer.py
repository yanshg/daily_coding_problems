#!/usr/bin/python

"""

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.

"""

# Idea:  Sorting issue.
#
# 1. Find number of digits in the largest number. Let number of digits be l.
# 2. Create extended version of all numbers. each number have n+1 digits formed by concatenating the number of with itself and truncating extra digits.
# 3. Sort original numbers according to their extended values.
# 4. Concatenating the sorted numbers produces th required result.


def form_largest_integer(arr):
    l=len(str(max(arr)))+1
    str_arr=list(map(str,arr))
    extval=[ ((s*l)[:l],s) for s in str_arr ]
    extval.sort(key=lambda x:x[0],reverse=True)
    return int(''.join([ x[1] for x in extval ]))

assert form_largest_integer([10, 7, 76, 415])==77641510
