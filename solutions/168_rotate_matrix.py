#!/usr/bin/python

"""
This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""

def rotate_matrix_helper(matrix,x,n):
    if n<=1:
        return matrix

    # rotate the outer cycle
    for i in range(n-1):
        matrix[x][x+i],matrix[x+n-i-1][x],matrix[x+n-1][x+n-1-i],matrix[x+i][x+n-1]=\
                matrix[x+n-i-1][x],matrix[x+n-1][x+n-1-i],matrix[x+i][x+n-1],matrix[x][x+i]

    # rotate the inner cycle
    return rotate_matrix_helper(matrix,x+1,n-2)

def rotate_matrix(matrix):
    return rotate_matrix_helper(matrix,0,len(matrix))

assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

