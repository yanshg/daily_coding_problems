#!/usr/bin/python

"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B

"""

# Use DFS variant.

def helper(matrix,rows,cols,x,y,orig_color,new_color,visited=set()):
    if x<0 or x>=rows or y<0 or y>=cols or \
       (x,y) in visited or \
       matrix[x][y] != orig_color:
        return

    visited.add((x,y))
    matrix[x][y]=new_color

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            helper(matrix,rows,cols,x+dx,y+dy,orig_color,new_color,visited)

    return

def replace_color_in_matrix(matrix,x,y,color):
    helper(matrix,len(matrix),len(matrix[0]),x,y,matrix[x][y],color,set())
    return matrix

def helper1(matrix,rows,cols,x,y,orig_color,new_color):
    if x<0 or x>=rows or y<0 or y>=cols or \
       matrix[x][y] != orig_color:
        return

    matrix[x][y]=-1

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            helper(matrix,rows,cols,x+dx,y+dy,orig_color,new_color)

    matrix[x][y]=new_color
    return

def replace_color_in_matrix1(matrix,x,y,color):
    helper1(matrix,len(matrix),len(matrix[0]),x,y,matrix[x][y],color)
    return matrix

matrix= [['B','B','W'],
         ['W','W','W'],
         ['W','W','W'],
         ['B','B','B']]

matrix1=[['B','B','G'],
         ['G','G','G'],
         ['G','G','G'],
         ['B','B','B']]
#assert replace_color_in_matrix(matrix,2,2,'G')==matrix1
assert replace_color_in_matrix1(matrix,2,2,'G')==matrix1
