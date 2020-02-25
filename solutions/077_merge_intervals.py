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

    stack=[intervals[0]]

    for i in range(1,len(intervals)):
        last_start,last_end=stack[-1]
        start,end=intervals[i]

        if last_end<=start:
            # Not overlap
            stack.append(intervals[i])
        elif last_end<end:
            # Some overlap, merge these 2 intervals
            stack.pop()
            stack.append((last_start,end))

    return stack

assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)])==[(1, 3), (4, 10), (20, 25)]
