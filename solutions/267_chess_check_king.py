#!/usr/bin/python

"""

This problem was asked by Oracle.

You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board. The only pieces on the board are the black king and various white pieces. Given this matrix, determine whether the king is in check.

For details on how each piece moves, see here.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..

You should return True, since the bishop is attacking the king diagonally.

"""

from collections import defaultdict

def get_pieces(board):
    pieces=defaultdict(list)

    # get position for all pieces
    for r in range(len(board)):
        for c in range(len(board[0])):
            piece=board[r][c]
            if piece!='.':
                pieces[piece]+=[(r,c)]

    return pieces

def is_piece_check(piece_t,piece,king,pieces):
    pr,pc=piece
    kr,kc=king
    dr,dc=pr-kr,pc-kc

    # Check if Knight is checking
    if piece_t=='N' and abs(dr*dc)==2:
        return True

    # Check if Pawn is checking
    if piece_t=='P' and (dr==1 and abs(dc)==1):
        return True

    # Check if Rook is checking
    if piece_t=='R' and (dr==0 or dc==0):
        return True

    # Check if Bishop is checking
    if piece_t=='B' and abs(dr)==abs(dc):
        return True

    # Check if Queen is checking
    if piece_t=='Q' and (dr==0 or dc==0 or abs(dr)==abs(dc)):
        return True

    return False

def is_check(board):
    pieces=get_pieces(board)

    if 'K' not in pieces:
        return False

    king=pieces['K'][0]
    for piece_t in pieces.keys():
        for piece in pieces[piece_t]:
            if is_piece_check(piece_t,piece,king,pieces):
                return True

    return False

board=[
    ['.','.','.','K','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','B','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','P','.'],
    ['.','.','.','.','.','.','.','R'],
    ['.','.','N','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','Q','.','.'],
]
assert is_check(board)
