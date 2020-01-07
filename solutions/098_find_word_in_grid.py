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
#        Base cases:  1. if out of the board, return []
#                     2. if finish checking, return [ path ]
#                     3. if visited, return []
#                     4. if not matched, return []

def helper(board,rows,cols,x,y,word,path=[],visited=set()):
    if x>=rows or x<0 or y>=cols or y<0:
        return []

    if not word:
        return path

    coord="{}-{}".format(x,y)
    if coord in visited:
        return []

    if board[x][y]!=word[0]:
        return []

    path+=[coord]
    visited.add(coord)

    moves=[ (0,1),(0,-1),(1,0),(-1,0) ]
    for dx,dy in moves:
        extended_path=helper(board,rows,cols,x+dx,y+dy,word[1:],path[:],visited.copy())
        if extended_path:
            return extended_path

    return []

def exists(board,word):
    rows,cols=len(board),len(board[0])
    for x in range(rows):
        for y in range(cols):
            path=helper(board,rows,cols,x,y,word,[],set())
            if path:
                print("word: ", word, "path: ", path)
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
