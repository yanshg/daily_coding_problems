#!/usr/bin/python

"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""

# f(n)=f(n-1) + f(n-2)

def staircase_ways_dp(n,steps=[1,2]):
    if n<0:
        return 0

    if n==0:
        return 1

    return sum([staircase_ways_dp(n-step) for step in steps])


# Memorize

def staircase_ways(n,steps=[1,2]):
    cache=[0]*(n+1)
    cache[0]=1

    for i in range(1,n+1):
        cache[i]=sum([cache[i-step] for step in steps if i-step>=0 ])
    
    return cache[n]

assert staircase_ways_dp(4)==5
assert staircase_ways(4)==5
