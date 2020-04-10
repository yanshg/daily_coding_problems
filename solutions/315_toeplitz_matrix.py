#!/usr/bin/python

"""

This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2

Write a program to determine whether a given input is a Toeplitz matrix.

"""

# Idea:  Compare with top-left neighbor for each element
#
#        For each element (r, c), check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c]
#

def is_toeplitz_matrix(matrix):
    #return all([r==0 or c==0 or matrix[r-1][c-1]==val
    #              for r,row in enumerate(matrix)
    #                for c,val in enumerate(row) ])
    for r in range(1,len(matrix)):
        row=matrix[r]
        for c in range(1,len(row)):
            if matrix[r-1][c-1]!=matrix[r][c]:
                return False

    return True

matrix=[
    [ 1, 2, 3, 4, 8 ],
    [ 5, 1, 2, 3, 4 ],
    [ 4, 5, 1, 2, 3 ],
    [ 7, 4, 5, 1, 2 ],
]

assert is_toeplitz_matrix(matrix)

matrix[0][0]=2
assert not is_toeplitz_matrix(matrix)

