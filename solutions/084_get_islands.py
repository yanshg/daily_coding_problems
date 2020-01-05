#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

"""

# Idea: Use dynamic programming
#       Base cases:  1. if out of the matrix, return 0
#                    2. if visited, return 0
#                    3. if 0, return 0
#                    4, if 1, check all neighbors, and return 1

def check_island(matrix,rows,cols,x,y,visited):
    if (x<0 or x>=rows) or (y<0 or y>=cols):
        return 0

    if not matrix[x][y]:
        return 0

    coord="{}-{}".format(x,y)
    if coord in visited:
        return 0

    visited.add(coord)

    for dx in [1,0,-1]:
        for dy in [1,0,-1]:
            check_island(matrix,rows,cols,x+dx,y+dy,visited)

    return 1

def get_islands(matrix):
    islands=0
    visited=set();
    rows,cols=len(matrix),len(matrix[0])

    return sum([ check_island(matrix,rows,cols,i,j,visited) for i in range(rows) for j in range(cols) ])

matrix=[
    [1,0,0,0,0],
    [0,0,1,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [1,1,0,0,1],
    [1,1,0,0,1],
]

assert get_islands(matrix)==4

matrix=[
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [1,1,0,0,1],
    [1,1,0,0,1],
]

#assert get_islands(matrix)==2

