#!/usr/bin/python

"""

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].

"""

import math

def get_closest_points(points):
    pairs=[]

    n=len(points)
    min_distance=float('inf')
    min_pair=[]
    for i in range(0,n-1):
        x1,y1=points[i]
        for j in range(i+1,n):
            x2,y2=points[j]
            distance=math.hypot(x2-x1,y2-y1)
            if distance<min_distance:
                min_distance=distance
                min_pair=[points[i],points[j]]
    return min_pair


assert get_closest_points([(1,1),(-1,-1),(3,4),(6,1),(-1,-6),(-4,-3)])==[(1,1),(-1,-1)]

