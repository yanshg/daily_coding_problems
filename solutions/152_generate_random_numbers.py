#!/usr/bin/python

"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

"""

import random
import bisect
from collections import defaultdict

def generate_random_number(nums,prob_sums):
    assert len(nums)==len(prob_sums)
    r=random.random()
    i=bisect.bisect_left(prob_sums,r)
    return nums[i]

numbers=[1, 2, 3, 4]
probabilities=[0.1, 0.5, 0.2, 0.2]
assert sum(probabilities)==1

prob_sums=[]
sums=0
for prob in probabilities:
    sums+=prob
    prob_sums+=[sums]

num_experiments=100000
counts=defaultdict(int)

for i in range(num_experiments):
    n=generate_random_number(numbers,prob_sums)
    counts[n]+=1

for i,n in enumerate(numbers):
    p=round(float(counts[n])/num_experiments,1)
    assert p==probabilities[i]
