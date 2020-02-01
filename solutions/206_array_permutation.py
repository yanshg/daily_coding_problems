#!/usr/bin/python

"""
This problem was asked by Twitter.

A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

"""

# swap both the array[] and index[] elements of the 2 positions together

def array_permutation(arr,index):
    for i in range(len(arr)):
        ni=index[i]
        if ni!=i:
            arr[i],arr[ni]=arr[ni],arr[i]
            index[i],index[ni]=index[ni],index[i]
    return arr

assert array_permutation(["a","b","c"],[2,1,0])==["c","b","a"]
assert array_permutation(["a","b","c","d"],[3,1,0,2])==["c","b","d","a"]


