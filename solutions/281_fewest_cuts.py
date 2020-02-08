#!/usr/bin/python

"""

This problem was asked by LinkedIn.

A wall consists of several rows of wall of various integer lengths and uniform height. Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of wall. If the line goes through the edge between two wall, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the lengths of wall in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]

The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the wall in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, return the fewest number of wall that must be cut to create a vertical line.

"""

# Idea: use dict to record cuts

from collections import defaultdict

def fewest_cuts(wall):
    cuts=defaultdict(int)
    for row in wall:
        col=0
        for brick in row[:-1]:
            col+=brick
            cuts[col]+=1

    return len(wall)-max(cuts.values())

wall=[[3, 5, 1, 1],
      [2, 3, 3, 2],
      [5, 5],
      [4, 4, 2],
      [1, 3, 3, 3],
      [1, 1, 6, 1, 1]]

assert fewest_cuts(wall)==2



