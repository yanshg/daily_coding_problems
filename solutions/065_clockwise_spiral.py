#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

   1
   2
   3
   4
   5
   10
   15
   20
   19
   18
   17
   16
   11
   6
   7
   8
   9
   14
   13
   12

"""

# Idea:   First get the outter circle with clockwise sequence
#         Then get the inner circles one by one with same way.

def get_outter_circle(matrix,row,col,rows,cols):
    spiral=[]
    for c in range(col,col+cols):
        spiral.append(matrix[row][c])

    c=col+cols-1
    for r in range(row+1,row+rows):
        spiral.append(matrix[r][c])

    r=row+rows-1
    for c in range(col+cols-2,col,-1):
        spiral.append(matrix[r][c])

    for r in range(row+rows-1,row,-1):
        spiral.append(matrix[r][col])

    return spiral

def helper(matrix,row,col,rows,cols):
    if rows<=0 or cols<=0:
        return []

    return get_outter_circle(matrix,row,col,rows,cols) + helper(matrix,row+1,col+1,rows-2,cols-2)

def clockwise_spiral(matrix):
    return helper(matrix,0,0,len(matrix),len(matrix[0]))

matrix=[[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

assert clockwise_spiral(matrix)==[1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
