#!/usr/bin/python

"""

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.

"""

def helper(nums_arr,height,sum=0,last_index=0,path=[]):
    l=len(path)
    if l==height:
        return sum,path

    first=nums_arr[l][last_index]
    sum1,path1=helper(nums_arr,height,sum+first,last_index,path+[first])

    second=nums_arr[l][last_index+1]
    sum2,path2=helper(nums_arr,height,sum+second,last_index+1,path+[second])

    return (sum1,path1) if sum1>sum2 else (sum2,path2)


def get_maximum_weight_path(nums_arr):
    height=len(nums_arr)
    assert height>0

    first=nums_arr[0][0]
    sum,path=helper(nums_arr,height,first,0,[first])
    print("path: ", path)
    return path

assert get_maximum_weight_path([[1], [2, 3], [1, 5, 1]])==[1,3,5]
