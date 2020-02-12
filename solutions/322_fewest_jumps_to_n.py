#!/usr/bin/python

"""

This problem was asked by Flipkart.

Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.

"""

def helper(n,start,steps=0,path=[]):
    if start==n:
        path+=[n]
        print("path:", path)
        return steps,path

    if start<0 or start>n:
        return 0,[]

    steps_forward,path_forward=helper(n, start+steps+1, steps+1,path+[start])
    steps_backward,path_fbackward=helper(n, start-steps-1, steps+1,path+[start])

    if steps_forward>0 and steps_backward>0:
        return (steps_forward,path_forward) if steps_forward<=steps_backward else (steps_backward,path_fbackward)
    elif steps_forward>0:
        return steps_forward,path_forward
    elif steps_backward>0:
        return steps_backward,path_fbackward

    return 0,[]

def fewest_jumps(n):
    steps,path=helper(n,0,0,[])
    print("Steps:", steps, "Path: ", path)
    return steps

assert fewest_jumps(10)==4
assert fewest_jumps(11)==6
