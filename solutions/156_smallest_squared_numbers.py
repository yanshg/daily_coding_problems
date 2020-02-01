#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3**2 + 2**2 = 9 + 4.

Given n = 27, return 3 since 27 = 3**2 + 3**2 + 3**2 = 9 + 9 + 9.

"""

def get_candidates(n):
    candidates=[]
    i=2
    while i<n//2 and i*i<=n:
        candidates+=[i]
        i+=1
    return candidates

def helper(n,candidates,path_so_far=[],all_paths=[]):
    if n==0 and path_so_far:
        all_paths.append(path_so_far)
        return

    for i in candidates:
        if i*i<=n:
            helper(n-i*i, candidates, path_so_far+[i], all_paths)

def get_smallest_squared_integers(n):
    candidates=get_candidates(n)
    all_paths=list()
    helper(n,candidates,[],all_paths)
    print("all_paths: ", all_paths)
    return min(list(map(len,all_paths)))


assert get_smallest_squared_integers(13)==2
assert get_smallest_squared_integers(27)==3
