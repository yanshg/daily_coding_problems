#!/usr/bin/python

"""

This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

"""

# O(N^3)
def pythagorean_triplet_bruteforce(nums):
    nums.sort()
    n=len(nums)
    return [(nums[i],nums[j],nums[k]) for i in range(n-2) for j in range(i,n-1) for k in range(j,n) if nums[i]*nums[i]+nums[j]*nums[j]==nums[k]*nums[k] ]

# O(N^2)
import math
def pythagorean_triplet(nums):
    n=len(nums)
    snums=list(map(lambda x:x*x, sorted(nums)))

    results=[]
    hashmap=set(snums[0:2])
    for i in range(2,n):
        for j in range(0,i-1):
            if (snums[i]-snums[j]) in hashmap:
                results+=[ (math.sqrt(snums[j]), math.sqrt(snums[i]-snums[j]), math.sqrt(snums[i])) ]
        hashmap.add(snums[i])

    return results

assert pythagorean_triplet_bruteforce([2,3,4,2,5,10,12,16,13])==[(3,4,5),(5,12,13)]
assert pythagorean_triplet([2,3,4,2,5,10,12,16,13])==[(3,4,5),(5,12,13)]
