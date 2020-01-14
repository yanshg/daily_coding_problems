#!/usr/bin/python

"""
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?

"""

def rotate_list_once(arr):
    first=arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1]=first
    return arr

def rotate_list_alt(arr,k):
    k%=len(arr)
    for i in range(k):
        rotate_list_once(arr)
    return arr

def rotate_list(arr,k):
    k%=len(arr)
    return arr[k:] + arr[:k]

assert rotate_list([1,2,3,4,5,6],2) == [3,4,5,6,1,2]
assert rotate_list_alt([1,2,3,4,5,6],2) == [3,4,5,6,1,2]
