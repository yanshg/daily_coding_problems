#!/usr/bin/python

"""

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

"""

import random

def unbiased_toss():
    return 1 if random.random()<0.7 else 0

num_experiments=10000
count=0
for i in range(num_experiments):
    count+=unbiased_toss()

assert round(float(count)/num_experiments,1)==0.7

