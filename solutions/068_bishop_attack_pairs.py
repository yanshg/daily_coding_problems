#!/usr/bin/python

"""

This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

"""

# y=x+b  => y-x = b
# y=-x+c => y+x = c
#
# Just to check if any 2 points with same value of y-x,  or any 2 points with same value of y+x
#
# Use hashmap to reduct to O(N)

from collections import defaultdict

def count_attack_bishop_pairs(m,bishops):
    hash_y_minus_x=defaultdict(list)
    hash_y_plus_x=defaultdict(list)

    for x,y in bishops:
        hash_y_minus_x[y-x]+=[(x,y)]
        hash_y_plus_x[y+x]+=[(x,y)]

    return sum([ 1 for k in hash_y_minus_x if len(hash_y_minus_x[k])>1 ] + \
               [ 1 for k in hash_y_plus_x if len(hash_y_plus_x[k])>1 ])

assert count_attack_bishop_pairs(5, [ (0,0), (1,2), (2,2), (4,0) ])==2

