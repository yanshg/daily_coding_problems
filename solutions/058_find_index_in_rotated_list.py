#!/usr/bin/python

"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

"""


# Idea:  the array could be seperated with 2 sorted sub array. use special binary searching algorithm.
#
#        2 scenarios:
#            1. element is on the first sorted sub array
#            2. element is on the second sorted sub array
#
#        3 cases for each above 2 scenarios:
#            1. middle element is right the searching element
#            2. middle element is smaller than the searching element
#            3. middle element is larger than the searching element


def rotated_search(arr, element, left, right):
    if left>right:
        return None

    mid=(left+right)//2
    if arr[mid]==element:
        return mid
    elif arr[mid]<element:
        if arr[left]<=element:
            # element is on the first sorted sub array
            return rotated_search(arr, element, left, mid)
        else:
            # element is on the second sorted sub array
            return rotated_search(arr, element, mid, right)
    else:
        if arr[left]>=element:
            # element is on the first sorted sub array
            return rotated_search(arr, element, left, mid)
        else:
            # element is on the second sorted sub array
            return rotated_search(arr, element, mid, right)

def search_element(arr, element):
    return rotated_search(arr, element, 0, len(arr))

assert search_element([13, 18, 25, 2, 8, 10], 2) == 3
assert search_element([13, 18, 25, 2, 8, 10], 18) == 1
assert search_element([25, 2, 8, 10, 13, 18], 8) == 2
assert search_element([8, 10, 13, 18, 25, 2], 8) == 0
