#!/usr/bin/python

"""

This problem was asked by Two Sigma.

A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times, where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on.

After k moves, what is the probability that the knight remains on the board?

"""
import random

def check_if_on_board(x,y,k):
    if x<0 or x>=8 or y<0 or y>=8:
        return False

    if k==0:
        return True

    moves=[(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    index=int(random.random()*8)
    dx,dy=moves[index]
    return check_if_on_board(x+dx,y+dy,k-1)

x0,y0=4,4
k=6

num_experiments=10000

count=0
for i in range(num_experiments):
    if check_if_on_board(x0,y0,k):
        count+=1

prob=round(float(count)/num_experiments,2)

print("Probability:", prob)

