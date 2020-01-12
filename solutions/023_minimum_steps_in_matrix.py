#!/usr/bin/python

"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

"""

# Idea:  get the pathes for 4 different directions, compare and get the path with minimum number of steps
#
#                 ^                         Base cases: 1. if out of the matrix, return []
#                 |                                     2. if visited, return []
#         <-  base point ->                             3. if meet wall, return []
#                 |                                     4. if get to end point, return the path.
#                 v
#                                           Notes:  record the intermediate data for path, visited.
#                                                   return the final path with minimum steps

def helper(matrix,rows,columns,start_point,end_point,path=[],visited=set()):
    (sx,sy)=start_point
    if sx<0 or sx>=rows or sy<0 or sy>=columns:
        return []

    coord="{}-{}".format(sx,sy)
    if coord in visited:
        return []

    visited.add(coord)

    if matrix[sx][sy]=='t':
        return []

    path+=[ coord ]

    if start_point==end_point:
        print("path:",path)
        return path

    # Notes: use the copy of intermediate results for path and visited
    direction_points=[(sx+1,sy),(sx-1,sy),(sx,sy-1),(sx,sy+1)]
    pathes=[ helper(matrix,rows,columns,point,end_point,path[:],visited.copy()) for point in direction_points ]

    pathes=[ p for p in pathes if p ]
    return min(pathes,key=len) if pathes else []

def get_min_steps(matrix,start_point,end_point):
    path=helper(matrix,len(matrix),len(matrix[0]),start_point,end_point,[],set())
    return len(path)-1 if path else 0

matrix= [['f', 'f', 'f', 'f'],
         ['t', 't', 'f', 't'],
         ['f', 'f', 'f', 'f'],
         ['f', 'f', 'f', 'f']]

assert get_min_steps(matrix,(3,0),(0,0))==7
assert get_min_steps(matrix,(0,0),(0,0))==0
assert get_min_steps(matrix,(0,1),(0,0))==1
assert get_min_steps(matrix,(3,0),(0,3))==6
