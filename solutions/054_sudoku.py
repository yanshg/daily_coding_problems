#!/usr/bin/python

"""

This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

"""

# Articles:  https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

# Using backtracking algorithm:

ROWS = 9
COLS = 9

def is_valid(board,row,col,val):
    # check column
    for r in range(ROWS):
        if r!=row and board[r][col] == val:
            return False

    # check row
    for c in range(COLS):
        if c!=col and board[row][c] == val:
            return False

    # check box
    box_r,box_c=(row//3)*3,(col//3)*3
    for r in range(box_r,box_r+3):
        for c in range(box_c,box_c+3):
            if r!=row and c!=col and board[r][c]==val:
                return False

    return True

def solve_sudoku(board,row=0,col=0):
    # if get the end of the row, go to the beginning of next row
    if col==COLS:
        return solve_sudoku(board,row+1,0)

    # if finished the last row, return.
    if row==ROWS:
        print_sudoku(board)
        return True

    # if the cell is already solved, go to next cell
    if board[row][col]:
        return solve_sudoku(board,row,col+1)

    for n in range(1,10):
        digit=str(n)
        if is_valid(board,row,col,digit):
            board[row][col] = digit
            if solve_sudoku(board,row,col+1):
                return True
            board[row][col] = ''

    return False

def print_sudoku(board):
    separator = '|'+'-'*23+"|\n"

    string = separator
    for row,digits in enumerate(board):
        string += '|'
        for col,digit in enumerate(digits):
            string += ' ' + (digit if digit else ' ')
            if (col+1)%3 == 0:
                string += ' |'
        string += '\n'

        if (row+1)%3==0:
            string+=separator

    print(string)

board = [
    ['7', '8', '',  '4', '',  '',  '1', '2', '' ],
    ['6', '',  '',  '',  '7', '5', '',  '',  '9'],
    ['',  '',  '',  '6', '',  '1', '',  '7', '8'],
    ['',  '',  '7', '',  '4', '',  '2', '6', '' ],
    ['',  '',  '1', '',  '5', '',  '9', '3', '' ],
    ['9', '',  '4', '',  '6', '',  '',  '',  '5'],
    ['',  '7', '',  '3', '',  '',  '',  '1', '2'],
    ['1', '2', '',  '',  '',  '7', '4', '',  '' ],
    ['',  '4', '9', '2', '',  '6', '',  '',  '7']
]

print_sudoku(board)
solve_sudoku(board,0,0)

