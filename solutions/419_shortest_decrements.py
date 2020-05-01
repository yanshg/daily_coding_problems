#!/usr/bin/python

"""

This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

    You may decrement N to N - 1.
    If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

"""

from collections import deque
import math

def get_decrements(n):
    end=int(math.sqrt(n))
    return [n-1] + [ n//i for i in range(end,1,-1) if n%i==0 ]

# BFS
def get_shortest_decrements(n):
    dq=deque([(n,[n])])
    while dq:
        num,path=dq.popleft()
        if num==1:
            return path

        for d in get_decrements(num):
            dq.append((d,path+[d]))

    return None

assert get_shortest_decrements(100)==[100,10,9,3,2,1]
