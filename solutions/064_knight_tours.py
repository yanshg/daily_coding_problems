#!/usr/bin/python

"""

This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

"""

# Idea: Use dynamic programming
#       Base cases:  1. if out of the board, return 0
#                    2. if visited, return 0
#                    3. if all squares are visited, return 1

def helper(n,x,y,path=[],visited=set()):
    if x>=n or x<0 or y>=n or y<0:
        return 0

    coord="{}-{}".format(x,y)
    if coord in visited:
        return 0

    path+=[coord]
    visited.add(coord)
    if len(visited)==n*n:
        print("path: ", path)
        return 1

    moves=[ (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2) ]
    return sum([ helper(n, x+dx, y+dy, path[:], visited.copy()) for dx,dy in moves ])

def knight_tours(n):
    return sum([ helper(n,x,y,[],set()) for x in range(n) for y in range(n) ])

assert knight_tours(4) == 0
assert knight_tours(5) == 1728
