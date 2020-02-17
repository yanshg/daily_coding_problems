#!/usr/bin/python

"""

This problem was asked by Flipkart.

Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}


"""


# Idea:  Use Graph BFS algorithm 
# 
#        Consider the given snake and ladder board as a directed graph with number of vertices equal to the number of cells in the board.
#        The problem reduces to finding the shortest path in a graph.
#        Every vertex of the graph has an edge to next six vertices if next 6 vertices do not have a snake or ladder.
#        If any of the next six vertices has a snake or ladder, then the edge from current vertex goes to the top of the ladder
#        or tail of the snake.
#
#        Since all edges are of equal weight, we can efficiently find shortest path using Breadth First Search of the graph. 

from collections import deque

LENGTH=100

def init_board(snakes,ladders):
    board=[0] * (LENGTH+1)
    for i in range(LENGTH+1):
        board[i]=i

    for start,end in snakes.items():
        board[start]=end

    for start,end in ladders.items():
        board[start]=end

    return board

def minimum_turns(snakes,ladders):
    board=init_board(snakes,ladders)
    #print("board: ", board)

    start,end=1,LENGTH
    turns=0
    visited=set()

    dq=deque([(start,turns)])
    while dq:
        start,turns=dq.popleft()
        turns+=1

        for steps in range(1,7):
            next=start+steps
            if next>=end:
                return turns
            elif next not in visited:
                visited.add(next)
                visited.add(board[next])
                dq.append((board[next],turns))

    return turns


snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
assert minimum_turns(snakes,ladders)==7

