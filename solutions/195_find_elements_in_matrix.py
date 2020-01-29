#!/usr/bin/python

"""

This problem was asked by Google.

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1,  3,  7,  10, 15, 20],
 [2,  6,  9,  14, 22, 25],
 [3,  8,  10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

"""

def get_smaller_and_greater(matrix,i1,j1,i2,j2):
    rows,cols=len(matrix),len(matrix[0])
    num1,num2=matrix[i1][j1],matrix[i2][j2]
    smaller,greater=(num1,num2) if num1<num2 else (num2,num1)
    return sum([int(matrix[i][j]<smaller or matrix[i][j]>greater) for i in range(rows) for j in range(cols) ])


matrix=[ [1,  3,  7,  10, 15, 20],
         [2,  6,  9,  14, 22, 25],
         [3,  8,  10, 15, 25, 30],
         [10, 11, 12, 23, 30, 35],
         [20, 25, 30, 35, 40, 45] ]

assert get_smaller_and_greater(matrix,1,1,3,3)==14

