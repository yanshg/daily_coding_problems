#!/usr/bin/python

"""

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

"""


def rotate_array(arr, k):
    if k<=0:
        return arr

    l=len(arr)
    assert k<l
    #arr[:]=arr[-k:]+arr[:-k]

    tmp=arr[l-1]
    for i in range(l-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=tmp

    return rotate_array(arr,k-1)


arr = [1, 2, 3, 4, 5]
rotate_array(arr, 2)
assert arr == [4, 5, 1, 2, 3]
rotate_array(arr, 2)
assert arr == [2, 3, 4, 5, 1]
rotate_array(arr, 4)
assert arr == [3, 4, 5, 1, 2]
