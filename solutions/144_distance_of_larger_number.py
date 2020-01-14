#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

# Give one example [ 7, 3, 0, 5, 4 ], for 3, the nearest larger number is '7'
# Sort above list as:
# sorted_index, index, value
# 0,            2,     0
# 1,            1,     3
# 2,            4,     4
# 3,            3,     5
# 4,            0,     7

def get_mapping_index(arr):
    sorted_tuples=[ (x,i) for i,x in enumerate(arr) ]
    sorted_tuples.sort(key=lambda x: x[0])

    mapping=dict()
    l=len(arr)
    for k,(x,i) in enumerate(sorted_tuples):
        min_dist=l
        for m in range(k+1,l):
            (nx,ni)=sorted_tuples[m]
            dist=abs(ni-i)
            if dist<min_dist:
                min_dist=dist
                mapping[i]=ni

    return mapping


def nearest_larger(arr, index):
    mapping=get_mapping_index(arr)

    if index in mapping:
        return mapping[index]

    return None

assert nearest_larger([4, 1, 3, 5, 6], 0)==3
