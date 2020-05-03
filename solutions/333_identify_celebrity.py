#!/usr/bin/python

"""

This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

"""

# Idea:
#     |-|-|-|-|-|-|-|-|-|-|-|
#      |                   |
#      A ->             <- B
#
#     If A know B, then A can not be celebrity, Discard A (A+=1), and B may be celebrity
#     If A donot know B, then B can not be celebrity, Discard B (B-=1), and A may be celebrity
#
#     The final A should be the celebrity
#
#     Test cases:
#         1.  1 celebrity
#         2.  0 celebrity
#         3.  2 celebrity

def knows(matrix,a,b):
    if a<0 or a>=len(matrix) or b<0 or b>=len(matrix[0]):
        return 0
    return matrix[a][b]

# O(N^2)
def get_celebrity_bruteforce(matrix):
    n=len(matrix)
    for b in range(n):
        if all([knows(matrix,a,b) and not knows(matrix,b,a) for a in range(n) if a!=b]):
            return b
    return None

# O(N)
def get_celebrity(matrix):
    n=len(matrix)
    a,b=0,n-1
    while a<b:
        if knows(matrix,a,b):
            a+=1
        else:
            b-=1

    # a may be celebrity, verify with all others
    if all([knows(matrix,b,a) and not knows(matrix,a,b) for b in range(n) if a!=b]):
        return a

    return None

matrix=[
    [ 0, 0, 1, 0 ],
    [ 0, 0, 1, 0 ],
    [ 0, 0, 0, 0 ],
    [ 0, 0, 1, 0 ]
]

assert get_celebrity_bruteforce(matrix)==2
assert get_celebrity(matrix)==2


