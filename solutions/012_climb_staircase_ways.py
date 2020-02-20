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

# If only need get the number of ways, then need memorize

def climb_staircase_ways(step_num, step_sizes={1,2},path=[],ways=[]):
    for s in step_sizes:
        if s==step_num:
            ways.append(path+[s])
        elif s<step_num:
            climb_staircase_ways(step_num-s, step_sizes, path+[s], ways)
    return ways

def get_climb_staircase_ways_number(step_num, step_sizes={1,2}):
    return len(climb_staircase_ways(step_num, step_sizes, [], []))

assert climb_staircase_ways(4)==[[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
