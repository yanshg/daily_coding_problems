#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

# Idea: Use 'mid' pointer to determine if swap lower or higher characters
#
#       |    'R's    |     'G's    |      Unknown      |    'B's     |
#       |------------|-|-----------|-|---------------|-|-------------|
#                    low           mid               high
#
# arr[:low]:     Strictly 'R's
# arr[low:mid]:  Strictly 'G's
# arr[mid:high]: Unknown
# arr[high:]:    Strictly 'B's
#
def partition(arr):
    low,mid,high=0,0,len(arr)-1
    while mid<=high:
        if arr[mid]=='R':
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]=='G':
            mid+=1
        elif arr[high]=='B':
            high-=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

assert partition(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
