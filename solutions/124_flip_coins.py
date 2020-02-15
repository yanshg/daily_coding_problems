#!/usr/bin/python

"""
This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

"""

import random

def flip_coins(n):
    rounds=0
    while True:
        rounds+=1
        for i in range(n):
            if (random.random()<0.5):
                n-=1
        if n<=1:
            break
    return rounds

num=64
for sample in range(100):
    print("#{:3d}: rounds to flip {} coins: {}".format(sample, num, flip_coins(num)))


from math import log2, ceil

def get_num_expected(coin_tosses):
    return ceil(log2(coin_tosses))

assert get_num_expected(1) == 0
assert get_num_expected(2) == 1
assert get_num_expected(100) == 7
assert get_num_expected(200) == 8
