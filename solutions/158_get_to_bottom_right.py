#!/usr/bin/python

"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.

"""

# use DP table
def get_ways(matrix):
    rows,cols=len(matrix),len(matrix[0])
    DP=[ [1 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==1:
                DP[i][j]=0
            elif i==0 and j>0:
                DP[i][j] = DP[i][j-1]
            elif i>0 and j==0:
                DP[i][j] = DP[i-1][j]
            elif i>0 and j>0:
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
    return DP[-1][-1]

matrix=[[0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]]

assert get_ways(matrix)==2

