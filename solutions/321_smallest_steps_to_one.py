#!/usr/bin/python

"""

This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

    You may decrement N to N - 1.
    If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

"""

def get_factors(n):
    factors=[]
    p=2
    while p*p<=n:
        if n%p==0:
            factors.append(n//p)
        p+=1
    return factors

def helper(start,steps=0,path=[]):
    if start==1:
        path+=[start]
        #print("path: ",path)
        return steps,path

    factors=get_factors(start)
    min_steps,min_path=0,[]
    for next_start in [start-1]+factors:
        steps1,path1=helper(next_start,steps+1,path+[start])
        if steps1>0 and (min_steps==0 or steps1<=min_steps):
            min_steps,min_path=(steps1,path1)

    return min_steps,min_path

def steps_to_one(n):
    factors=get_factors(n)
    steps,path=helper(n,0,[])
    print("Steps:", steps, "Path:",path)
    return steps

assert steps_to_one(100)==5
