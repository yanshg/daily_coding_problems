#!/usr/bin/python

"""

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |


"""

# Article: https://www.cnblogs.com/lz87/p/11518225.html

# Idea: 
#
#    If all Quxes has the same color, return the length of the line.
#    If the parities of each color are equal, return 2.
#    If the parities of each color are different, return 1.

from collections import defaultdict,Counter

def fuse_quxes(quxes):
    counts=defaultdict(int)
    for qux in quxes:
        counts[qux]+=1

    n=len(quxes)
    reds,greens,blues=counts['R'],counts['G'],counts['B']
    if reds==n or greens==n or blues==n:
        return n

    if reds%2==greens%2 and reds%2==blues%2:
        return 2

    return 1


def fuse_quxes_dp(quxes):
    n=len(quxes)
    if len(set(quxes))==1:
        return n

    RGB_set={'R','G','B'}

    #print(quxes)
    for i in range(n-1):
        if quxes[i]!=quxes[i+1]:
            merged=list(RGB_set-{quxes[i],quxes[i+1]})
            return fuse_quxes_dp(quxes[:i]+merged+quxes[i+2:])

assert fuse_quxes(['R', 'G', 'B', 'G', 'B']) == 1
assert fuse_quxes(['R', 'G', 'B', 'R', 'G', 'B']) == 2
assert fuse_quxes(['R', 'R', 'G', 'B', 'G', 'B']) == 2
assert fuse_quxes(['G', 'R', 'B', 'R', 'G']) == 1
assert fuse_quxes(['G', 'R', 'B', 'R', 'G', 'R', 'G']) == 2
assert fuse_quxes(['R', 'R', 'R', 'R', 'R']) == 5
assert fuse_quxes(['R', 'R', 'R', 'G', 'G', 'G', 'B', 'B', 'B']) == 2

assert fuse_quxes_dp(['R', 'G', 'B', 'G', 'B']) == 1
assert fuse_quxes_dp(['R', 'G', 'B', 'R', 'G', 'B']) == 2
assert fuse_quxes_dp(['R', 'R', 'G', 'B', 'G', 'B']) == 2
assert fuse_quxes_dp(['G', 'R', 'B', 'R', 'G']) == 1
assert fuse_quxes_dp(['G', 'R', 'B', 'R', 'G', 'R', 'G']) == 2
assert fuse_quxes_dp(['R', 'R', 'R', 'R', 'R']) == 5
#assert fuse_quxes_dp(['R', 'R', 'R', 'G', 'G', 'G', 'B', 'B', 'B']) == 2
