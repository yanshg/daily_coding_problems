#!/usr/bin/python

"""
This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

"""

import math

def point_distance(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return math.hypot(x1-x2,y1-y2)

def get_nearest_k_points(points,central_point,k):
    if len(points)<=k:
        return points

    sorted_points=sorted(points, key=lambda x: point_distance(central_point, x))
    return sorted_points[:k]

assert get_nearest_k_points([(0, 0), (5, 4), (3, 1)], (1,2), 2)==[(0,0),(3,1)]
