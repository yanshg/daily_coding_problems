#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3**2 + 2**2 = 9 + 4.

Given n = 27, return 3 since 27 = 3**2 + 3**2 + 3**2 = 9 + 9 + 9.

"""

def get_candidates(n):
    candidates=[1]
    i=2
    while i<=n//2 and i*i<=n:
        candidates+=[i]
        i+=1
    return candidates

def helper(n,candidates,path):
    if n==0:
        return path

    if n<0:
        return []

    smallest_path=[]
    for i in candidates:
        sub_path=helper(n-i*i, candidates, path+[i])
        if sub_path and \
            (not smallest_path or len(sub_path)<=len(smallest_path)):
            smallest_path=sub_path

    return smallest_path

def get_smallest_squared_integers(n):
    candidates=get_candidates(n)
    smallest_path=helper(n,candidates,[])
    print(smallest_path)
    return len(smallest_path)

assert get_smallest_squared_integers(13)==2
assert get_smallest_squared_integers(27)==3
