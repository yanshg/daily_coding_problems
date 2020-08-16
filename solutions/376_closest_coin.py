#!/usr/bin/python

"""

This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------

return (0, 4), since that coin is closest. This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]

"""

# BFS

from collections import deque

class Board:
    def __init__(self, rows, cols, coins):
        self.rows = rows
        self.cols = cols
        self.board = [ ['.'] * cols for r in range(rows) ]
        for r,c in coins:
            self.board[r][c] = 'o'

    def __repr__(self):
        return ''.join([ self.board[r][c] if c < self.cols else '\n' for r in range(self.rows) for c in range(self.cols+1) ])


    def get_closest_coin(self, start_point):
        visited=set()

        dq = deque([(start,0)])
        while dq:
            (r,c),distance = dq.popleft()
            if self.board[r][c] == 'o':
                return (r,c,distance)

            s="{}-{}".format(r, c)
            visited.add(s)

            for (dr,dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                s = "{}-{}".format(nr, nc)
                if nr >= 0 and nr < self.rows and nc >= 0 and nc < self.cols and \
                    s not in visited:
                    dq.append(((nr, nc), distance+1))

        return None

board = Board(4, 5, [(0, 4), (1, 0), (2, 0), (2, 4), (3, 2)])
print(board)

start = (0,2)
print("start point: ", start)
print("closet coin: ", board.get_closest_coin(start))
