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

def minimum_moves_in_grid(points):
    xs,ys=list(zip(*points))
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    x,y=points[0]
    path=helper(minx,maxx,miny,maxy,points,1,x,y,[],set())
    return len(path)-1 if path else 0

assert minimum_moves_in_grid([(0, 0), (1, 1), (1, 2)])==2
