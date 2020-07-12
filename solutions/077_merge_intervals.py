#!/usr/bin/python

"""

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

"""

# Idea: For interval issues, use stack

def merge_intervals(intervals):
    # Sort intervals with start time
    intervals.sort(key=lambda x:x[0])

    result=[]
    for current in intervals:
        if not result:
            result.append(current)
            continue

        last=result[-1]
        if last[1]<=current[0]:
            # Not overlap
            result.append(current)
        elif last[1]<current[1]:
            # Some overlap, merge these 2 intervals
            last[1]=current[1]

    return result

assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)])==[(1, 3), (4, 10), (20, 25)]
