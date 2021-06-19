#!/usr/bin/python

"""

This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

"""

# Idea: BFS should be better than DFS
#
#
#             <   ^   >                     Base cases: 1. if out of the matrix, return []
#              \  |  /                                  2. if get to one point, get to the next point
#         <-  base point ->                             3. if visited, return []
#              /  |  \                                  4. if get to last point, return the path.
#             <   v   >
#                                           Notes:  record the intermediate data for path, visited.
#                                                   return the final path with minimum steps


# BFS

from collections import deque

def minimum_moves_in_grid_bfs(points):
    xs,ys=zip(*points)
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    n=len(points)

    visited=set()
    start=points[0]
    dq=deque([(start,0,[start])])
    while dq:
        point,index,path=dq.popleft()
        #print("point:",point,"index:",index,"Path:",path)
        if index==n-1:
            print(path)
            return len(path)-1

        x,y=point
        visited.add(point)

        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
               nx,ny=x+dx,y+dy
               point=(nx,ny)

               if minx<=nx<=maxx and miny<=ny<=maxy and \
                   point not in visited:
                   if point==points[index+1]:
                       dq.clear()
                       dq.append((point,index+1,path+[point]))
                       visited.clear()
                       for point1 in path:
                           visited.add(point1)
                   else:
                       dq.append((point,index,path+[point]))

    return 0

assert minimum_moves_in_grid_bfs([(0, 0), (1, 1), (1, 2)])==2
assert minimum_moves_in_grid_bfs([(0, 0), (3, 3), (1, 2)])==5
