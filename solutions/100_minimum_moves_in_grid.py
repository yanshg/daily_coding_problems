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

# DFS

def helper(minx,maxx,miny,maxy,points,index,x,y,path=[],visited=set()):
    if x<minx or x>maxx or y<miny or y>maxy:
        return []

    if (x,y)==points[index] and index<len(points)-1:
        return helper(minx,maxx,miny,maxy,points,index+1,x,y,path[:],visited.copy())

    coord="{}-{}".format(x,y)
    if coord in visited:
        return []

    visited.add(coord)
    path+=[coord]

    if (x,y)==points[index] and index==len(points)-1:
        print("path: ",path)
        return path

    pathes=[ helper(minx,maxx,miny,maxy,points,index,x+dx,y+dy,path[:],visited.copy()) for dx in [-1,0,1] for dy in [-1,0,1] ]
    pathes=[ p for p in pathes if p ]
    return min(pathes, key=len) if pathes else []

def minimum_moves_in_grid_dfs(points):
    xs,ys=list(zip(*points))
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    x,y=points[0]
    path=helper(minx,maxx,miny,maxy,points,1,x,y,[],set())
    return len(path)-1 if path else 0


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
        print("point:",point,"index:",index,"Path:",path)
        if index==n-1:
            print(path)
            return len(path)-1

        x,y=point
        coord="{}-{}".format(x,y)
        visited.add(coord)

        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
               nx,ny=x+dx,y+dy

               coord="{}-{}".format(nx,ny)
               if nx<minx or nx>maxx or ny<miny or ny>maxy or \
                   coord in visited:
                   continue

               point=(nx,ny)
               if point==points[index+1]:
                   dq.append((point,index+1,path+[point]))
               else:
                   dq.append((point,index,path+[point]))

    return 0

assert minimum_moves_in_grid_dfs([(0, 0), (1, 1), (1, 2)])==2
assert minimum_moves_in_grid_bfs([(0, 0), (1, 1), (1, 2)])==2
