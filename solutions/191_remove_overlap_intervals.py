#!/usr/bin/python

"""

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.

"""
# Article:  https://zhuhan0.blogspot.com/2017/03/leetcode-non-overlapping-intervals.html

# Idea: 1. Sort the intervals with start time,
#       2  Iterate through the intervals and use a local variable "end" to keep track of the smallest end point of current overlapping intervals. The reason is that we want to delete all overlapping intervals except the one that has the smallest end point, so that the next interval won't overlap with it.
#       3. Once we iterate through a group of overlapping intervals, we update "end" to be the end point of the next interval.

def remove_overlapping_intervals(intervals):
    intervals.sort(key=lambda t:t[0])

    removes=0

    last_start,last_end=intervals[0]
    for i in range(1,len(intervals)):
        start,end=intervals[i]
        if last_end>start:
            last_end=min(last_end,end)
            removes+=1
        else:
            last_end=end

    return removes

assert remove_overlapping_intervals([ [1,2], [2,3], [3,4], [1,3] ])==1
assert remove_overlapping_intervals([ [1,2], [1,2], [1,2] ])==2
assert remove_overlapping_intervals([ [1,2], [2,3] ])==0
