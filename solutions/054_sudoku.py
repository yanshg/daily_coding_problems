#!/usr/bin/python

"""

This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

"""

# Articles:  https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

# Using backtracking algorithm:
#    Simply reverting back to the previous step or solution
#    as soon as we determine that our current solution cannot be continued into a complete one.
#
# Starting with an incomplete board:
#
#    Find some empty space
#    Attempt to place the digits 1-9 in that space
#    Check if that digit is valid in the current spot based on the current board
#        a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
#        b. If it is not valid, reset the square you just filled and go back to the previous step.
#        Once the board is full by the definition of this algorithm we have found a solution.

def is_valid(board,val,row=0,col=0):
    # check column
    for r in range(len(board)):
        if r!=row and board[r][col] == val:
            return False

    # check row
    for c in range(len(board[0])):
        if c!=col and board[row][c] == val:
            return False

    # check box
    box_r,box_c=(row//3)*3,(col//3)*3
    for r in range(box_r,box_r+3):
        for c in range(box_c,box_c+3):
            if r!=row and c!=col and board[r][c]==val:
                return False

    return True

def find_first_blank_cell(board,row=0,col=0):
    for r in range(row,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c]==0:
                return r,c
    return None,None

def solve_sudoku(board,row=0,col=0):
    # find first cell need evaluate
    (row,col)=find_first_blank_cell(board,row,col)
    if row is None:
        # finish puzzle
        print_sudoku(board)
        return board

    for digit in range(1,10):
        if is_valid(board,digit,row,col):
            board[row][col]=digit
            solve_sudoku(board,row,col)
            board[row][col]=0

    return None

def print_sudoku(board):
    bound='|'+'-'*23+"|\n"
    string=bound
    for row in range(len(board)):
        string+='| ' + \
                ' '.join(( str(x) if x!=0 else ' ') + ( ' |' if (col+1)%3==0 else '' ) for col,x in enumerate(board[row])) +\
                "\n"
        if (row+1)%3==0:
            string+=bound
    print(string)

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print_sudoku(board)
solve_sudoku(board)

