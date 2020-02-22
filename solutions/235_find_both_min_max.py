#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.

"""

# O(n)
def compare(n1,n2):
    return (n1,n2) if n1<n2 else (n2,n1)

def get_min_max(nums):
    n=len(nums)
    assert n>0

    min_so_far,max_so_far=nums[0],nums[0]
    for i in range(0,n,2):
        if i==n-1:
            smaller,bigger=nums[i],nums[i]
        else:
            smaller,bigger=compare(nums[i],nums[i+1])

        min_so_far=min(min_so_far,smaller)
        max_so_far=max(max_so_far,bigger)

    return min_so_far,max_so_far

def get_min_max_dp(nums):
    n=len(nums)
    if n==1:
        return nums[0],nums[0]

    if n==2:
        return compare(nums[0],nums[1])

    mid=n//2
    lmin,lmax=get_min_max_dp(nums[:mid])
    rmin,rmax=get_min_max_dp(nums[mid:])
    return min(lmin,rmin),max(lmax,rmax)


assert get_min_max([43,5,34,55,4,78,2,25,22])==(2,78)
assert get_min_max_dp([43,5,34,55,4,78,2,25,22])==(2,78)
