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

# O(N^2)
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

# Article: https://www.geeksforgeeks.org/maximum-path-sum-triangle/
#          https://www.geeksforgeeks.org/minimum-sum-path-triangle/
#

# Bottom up:
# 1. Start from the nodes on the bottom row, the max pathsum for these nodes are the values of the nodes themselves.
# 2. after that, max pathsum at the ith node of kth row would be the max of the pathsum of its two children + the node's value, :
#      memo[k][i] = max(memo[k+1][i], memo[k+1][i+1]) + A[k][i];
# OR
#    Simply set memo as a 1D array, and update it for kth row:
#      memo[i] = max(memo[i], memo[i+1]) + A[k][i];

def get_maximum_weight_path2(A):
    memo = [None] * len(A)
    n = len(A) - 1

    # For the bottom row
    for i in range(len(A[n])):
        memo[i] = A[n][i]

    for i in range(len(A) - 2, -1,-1):
        for j in range(len(A[i])):
            memo[j] = A[i][j] + max(memo[j], memo[j+1])

    return memo[0]

assert get_maximum_weight_path([[1], [2, 3], [1, 5, 1]])==[1,3,5]
assert get_maximum_weight_path2([[1], [2, 3], [1, 5, 1]])==9
