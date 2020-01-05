#!/usr/bin/python

"""

This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

"""

import random
from collections import defaultdict

def rand7():
    return random.randint(1,7)

def rand5():
    r=rand7()
    if r>5:
        return rand5()
    return r

num_experiments=100000
results=defaultdict(int)

for i in range(num_experiments):
    results[rand5()]+=1

print(results)

for i in range(1,6):
    assert round(float(results[i])/num_experiments,1) == 0.2


