#!/usr/bin/python

"""

This problem was asked by Airbnb.

An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing. The remaining tiles are labeled 1 through 8 but shuffled randomly. Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.

Design a class to represent the board, and find a series of steps to bring the board to the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].

"""

# Article:  https://www.cs.princeton.edu/courses/archive/spring18/cos226/assignments/8puzzle/index.html

# With graph BFS algorithm

from collections import deque

class PuzzleBoard():
    def __init__(self, board=None):
        """
        012
        345
        678
        """
        self.adjacent_map = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4,6],
            [1,3,5,7],
            [2,4,8],
            [3,7],
            [4,6,8],
            [5,7]
        ]
        self.final_board_str="123456780"
        self.board=board

    def __repr__(self):
        return ''.join([str(digit) if digit else '0' for row in self.board for digit in row])

    def print_board(self,board_str):
        print(''.join([ (c if c!='0' else ' ') + (' ' if (i+1)%3 else '\n') for i,c in enumerate(board_str)]))

    def next_boards(self, board_str):
        zero_index=board_str.index('0')
        next_boards=[]
        for index in self.adjacent_map[zero_index]:
            # Note: could NOT use str[index]=c to change string directly, must first convert string to list.
            next_str=list(board_str)
            next_str[index],next_str[zero_index]=next_str[zero_index],next_str[index]
            next_boards+=[''.join(next_str)]
        return next_boards

    # BFS
    def solve_bfs(self):
        start=str(self)
        end=self.final_board_str

        visited=set()
        dq=deque([(start,[start])])

        while dq:
            board,path=dq.popleft()
            if board==end:
                print("path: ",path)
                for b in path:
                    self.print_board(b)
                return path

            visited.add(board)

            for next_board in self.next_boards(board):
                if next_board not in visited:
                    dq.append([next_board,path+[next_board]])

        return []

    # Bidirectional BFS
    def solve_bibfs(self):
        start=str(self)
        end=self.final_board_str

        visited=set()
        q1={start: [start]}
        q2={end: [end]}

        while q1 and q2:
            if len(q1)>len(q2):
                q1,q2=q2,q1

            q3=dict()
            for board,path in q1.items():
                if board in q2:
                    if path[0] == start:
                        full_path=path[:-1]+list(reversed(q2[board]))
                    else:
                        full_path=q2[board]+list(reversed(path[:-1]))
                    print("path: ",full_path)
                    for b in full_path:
                        self.print_board(b)
                    return full_path

                visited.add(board)

                for next_board in self.next_boards(board):
                    if next_board not in visited \
                        and next_board not in q3:
                        q3[next_board]=path+[next_board]

            q1=q3

        return []

board=[[3,7,1],[8,5,2],[6,4,None]]
puzzle=PuzzleBoard(board)
puzzle.solve_bfs()
puzzle.solve_bibfs()

