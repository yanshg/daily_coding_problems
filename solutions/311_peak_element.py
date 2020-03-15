#!/usr/bin/python

"""

This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.

"""

# Idea:
#
#    There is always a peak element in the array, even for the following corner cases:
#        1) If array is sorted in strictly increasing order, the last element is always a peak element.
#        2) If array is sorted in strictly decreasing order, the first element is always a peak element.
#
#    Use Binary Search, we compare middle element with its neighbors.
#        1) If middle element is not smaller than any of its neighbors, then we return it.
#        2) If middle element is smaller than the its left neighbor, then there is always a peak in left half
#        3) If middle element is smaller than the its right neighbor, then there is always a peak in right half

def find_peak_element(arr):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        if low==high:
            return arr[low]
        if high-low==1:
            return arr[low] if arr[low]>arr[high] else arr[high]

        mid=(low+high)//2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return arr[mid]
        elif arr[mid-1]>arr[mid]:
            high=mid-1
        else:
            low=mid+1

    return None

assert find_peak_element([10,20,30,40,50])==50
assert find_peak_element([50,40,30,20,10])==50
assert find_peak_element([20,40,30,10,50])==40
assert find_peak_element([50,10,30,40,20])==40
