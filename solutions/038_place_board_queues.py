#!/usr/bin/python

"""

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

"""

# Add and validate queue one by one, and push into array for recording

def is_valid(board):
    current_row,current_col=len(board)-1,board[-1]
    for row,col in enumerate(board[:-1]):
        diff=abs(current_col-col)
        if diff==0 or diff==current_row-row:
            return False
    return True

def place_queues(n,board=[]):
    if n==len(board):
        print("board:", board)
        return 1

    count=0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += place_queues(n,board)
        board.pop()

    return count

assert place_queues(10)==724
