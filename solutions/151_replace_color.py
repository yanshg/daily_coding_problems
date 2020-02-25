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

# Use DFS or BFS. both are fine.

def helper(matrix,rows,cols,x,y,old_color,new_color,visited=set()):
    if x<0 or x>=rows or y<0 or y>=cols:
        return

    if matrix[x][y]!=old_color:
        return

    coord="{}-{}".format(x,y)
    if coord in visited:
        return

    visited.add(coord)

    matrix[x][y]=new_color

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            helper(matrix,rows,cols,x+dx,y+dy,old_color,new_color,visited.copy())

    return


def replace_color_in_matrix(matrix,x,y,color):
    helper(matrix,len(matrix),len(matrix[0]),x,y,matrix[x][y],color,set())
    return matrix

matrix= [['B','B','W'],
         ['W','W','W'],
         ['W','W','W'],
         ['B','B','B']]

matrix1=[['B','B','G'],
         ['G','G','G'],
         ['G','G','G'],
         ['B','B','B']]
assert replace_color_in_matrix(matrix,2,2,'G')==matrix1
