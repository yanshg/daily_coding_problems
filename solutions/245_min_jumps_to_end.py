#!/usr/bin/python

"""

This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

"""

# 'path' argument is used to verify the jump progress, it could be removed to save space.

def helper(arr,start,end,jumps_so_far,path=[]):
    if start==end:
        print("path: ", path)
        return jumps_so_far
    elif start>end:
        return 0

    min_jumps=0
    for steps in range(arr[start],0,-1):
        jumps=helper(arr,start+steps,end,jumps_so_far+1,path+[start+steps])
        if jumps>0:
            min_jumps=jumps if not min_jumps else min(min_jumps,jumps)

    return min_jumps

def get_min_steps_to_end(arr):
    return helper(arr,0,len(arr)-1,0,[])

assert get_min_steps_to_end([6, 2, 4, 0, 5, 1, 1, 4, 2, 9])==2


