#!/usr/bin/python

"""
This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""

def mysum(l,start,end):
    return sum(l[start:end])

assert mysum([1, 2, 3, 4, 5], 1, 3)==5
assert mysum([1, 2, 3, 4, 5], 2, 4)==7

class SubarraySumOptimizer:
    def __init__(self, arr):
        self.arr=arr
        self.larr=list([0])
        for num in arr:
            self.larr.append(num + self.larr[-1])

    def sum(self,start,end):
        if start<0 or end<0 or start>end:
            return 0

        l=len(self.arr)
        end=min(end, l)
        return self.larr[end]-self.larr[start]

sso=SubarraySumOptimizer([1, 2, 3, 4, 5])
print(sso.larr)

assert sso.sum(1,3)==5
assert sso.sum(2,4)==7
