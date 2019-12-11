#!/usr/bin/python

"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import math,random

def estimate_pi():
    inside,samples=0,0
    count_per_test=100000
    pi_approx=3.0

    while True:
        for i in range(count_per_test):
            inside+=math.hypot(random.random(),random.random())<=1
        samples+=count_per_test

        pi_prev=pi_approx
        pi_approx=4 * float(inside) / samples
        if abs(pi_approx-pi_prev) < 1e-5:
            return pi_approx

pi=estimate_pi()
print("pi: ",pi)
assert round(pi, 2)==3.14
