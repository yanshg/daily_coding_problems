#!/usr/bin/python

"""

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

"""

import random
from collections import defaultdict

def generate_random_num(n, excludes):
    r = random.randint(0, n-1)
    return r if r not in excludes else generate_random_num(n, excludes)

n,excludes=10,{1,4,5,6}

error_tolerance=0.005
expected_prob=round(1.0/(n-len(excludes)), 3)

num_experiments=100000
results=defaultdict(int)
for i in range(num_experiments):
    results[generate_random_num(n,excludes)]+=1

for num in results:
    prob=round(float(results[num])/num_experiments, 3)
    print("num: ", num, "probs: ", prob)
    assert expected_prob-error_tolerance <= prob <= expected_prob+error_tolerance
