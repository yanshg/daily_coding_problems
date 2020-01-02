#!/usr/bin/python

"""

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

"""

# Base cases:   1. out of the matrix, return 0
#               2. visited, return 0
#               3. reach the bottom-right, return 1

def helper(rows,cols,row=0,col=0,path=[],visited=set()):
    if col>=cols or row>=rows:
        return 0

    coord="{}-{}".format(row,col)
    if coord in visited:
        return 0

    visited.add(coord)
    path+=[coord]

    if row==rows-1 and col==cols-1:
        #print("path: ", path)
        return 1

    return helper(rows,cols,row+1,col,path[:],visited.copy()) + \
           helper(rows,cols,row,col+1,path[:],visited.copy())

def traverse_matrix(rows,cols):
    return helper(rows,cols,0,0,[],set())

assert not traverse_matrix(1, 0)
assert traverse_matrix(1, 1) == 1
assert traverse_matrix(2, 2) == 2
assert traverse_matrix(5, 5) == 70
