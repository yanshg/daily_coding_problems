#!/usr/bin/python

"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""


# Idea:  Sort the given interval based on ending point and mark smallest number as 'x'.
#        Sort the given interval based on starting point and mark the largest number as 'y'.
#        Answer is {x,y}

def get_smallest_cover(intervals):
    starts,ends=zip(*intervals)
    return {min(ends),max(starts)}

assert get_smallest_cover([[0, 3], [2, 6], [3, 4], [6, 9]])=={3,6}
