#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

"""

def word_in_matrix(matrix,word):
    for item in matrix + list(zip(*matrix)):
        str=''.join(item)
        if word in str:
            return True
    return False

matrix=[['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

assert word_in_matrix(matrix,'FOAM')
assert word_in_matrix(matrix,'MASS')
assert not word_in_matrix(matrix,'IPBW')
