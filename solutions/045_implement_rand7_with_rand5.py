#!/usr/bin/python

"""

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

"""

# https://www.geeksforgeeks.org/generate-integer-from-1-to-7-with-equal-probability/

from collections import defaultdict
from random import randint

def rand5():
    return randint(1, 5)

def rand7_with_randint():
    return randint(1, 7)


def rand7_with_rand5():
    i = 5*rand5() + rand5() - 5  # uniformly samples between 1-25
    if i < 22:
        return i % 7 + 1
    return rand7_with_rand5()


num_experiments = 100000
result_dict = defaultdict(int)
for _ in range(num_experiments):
    number = rand7_with_rand5()
    result_dict[number] += 1

desired_probability = 1.0 / 7
for number in result_dict:
    result_dict[number] = float(result_dict[number]) / num_experiments
print("result_dict: ", str(result_dict))

assert round(desired_probability, 2) == round(result_dict[number], 2)
