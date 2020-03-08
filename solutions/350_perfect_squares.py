#!/usr/bin/python

"""

This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:
 - Given N = 4, return 1 (4)
 - Given N = 17, return 2 (16 + 1)
 - Given N = 18, return 2 (9 + 9)

"""

def get_candidates(n):
    candidates=[1]
    i=2
    while i<=n//2 and i*i<=n:
        candidates+=[i]
        i+=1
    return list(reversed(candidates))

def helper(n,candidates,path=[]):
    if n==0 and path:
        #print("path,",path)
        return path

    if n<0:
        return []

    smallest_path=[]
    for c in candidates:
        sub_path=helper(n-c*c,candidates,path+[c])
        if sub_path and \
            (not smallest_path or len(sub_path)<len(smallest_path)):
            smallest_path=sub_path

    return smallest_path

def get_smallest_perfect_squares(n):
    candidates=get_candidates(n)
    smallest_path=helper(n,candidates,[])
    print("candidates:", candidates,"smallest path:",smallest_path)
    return len(smallest_path)

assert get_smallest_perfect_squares(4)==1
assert get_smallest_perfect_squares(17)==2
assert get_smallest_perfect_squares(18)==2
