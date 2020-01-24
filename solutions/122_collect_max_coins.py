#!/usr/bin/python

"""
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

"""


def helper(matrix,row,col,rows,cols):
    if row>=rows or col>=cols:
        return 0

    return matrix[row][col] + \
           max(helper(matrix,row+1,col,rows,cols), \
               helper(matrix,row,col+1,rows,cols))

def get_max_coins(matrix):
    if not matrix:
        return 0

    return helper(matrix,0,0,len(matrix),len(matrix[0]))

matrix=[[0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]]
assert get_max_coins(matrix)==12

matrix=[[0, 3, 1, 1],
        [2, 8, 9, 4],
        [1, 5, 3, 1]]
assert get_max_coins(matrix) == 25
