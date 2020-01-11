#!/usr/bin/python

"""

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

"""

# Idea:  Use dynamic programming method
#        Base cases:  1. if out of the board, return False
#                     2. if finish checking, return True
#                     4. if first char not matched, return False
#                     3. if visited, return False

def helper(board,rows,cols,x,y,word,path=[],visited=set()):
    if x>=rows or x<0 or y>=cols or y<0:
        return False

    if not word:
        print("path: ", path)
        return True if path else False

    if board[x][y]!=word[0]:
        return False

    coord="{}-{}".format(x,y)
    if coord in visited:
        return False

    path+=[coord]
    visited.add(coord)

    moves=[ (0,1),(0,-1),(1,0),(-1,0) ]
    for dx,dy in moves:
        if helper(board,rows,cols,x+dx,y+dy,word[1:],path[:],visited.copy()):
            return True

    return False

def exists(board,word):
    rows,cols=len(board),len(board[0])
    for x in range(rows):
        for y in range(cols):
            if helper(board,rows,cols,x,y,word,[],set()):
                return True
    return False

board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

assert exists(board,"ABCCED")
assert exists(board,"SEE")
assert not exists(board,"ABCB")
