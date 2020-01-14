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

def helper(matrix,rows,cols,x,y,path=[],visited=set()):
    if x<0 or x>=rows or y<0 or y>=cols:
        return 0

    if matrix[x][y]==1:
        return 0

    coord="{}-{}".format(x,y)
    if coord in visited:
        return 0

    path+=[coord]

    if x==rows-1 and y==cols-1:
        print("path: ",path)
        return 1

    visited.add(coord)

    return sum([ helper(matrix,rows,cols,x,y+1,path[:],visited.copy()), 
                 helper(matrix,rows,cols,x+1,y,path[:],visited.copy()) ])

def get_ways_to_bottom_right(matrix):
    return helper(matrix,len(matrix),len(matrix[0]),0,0,[],set())

matrix=[[0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]]

assert get_ways_to_bottom_right(matrix)==2

