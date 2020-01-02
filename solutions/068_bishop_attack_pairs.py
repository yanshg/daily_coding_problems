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

def count_attack_bishop_pairs(m,bishops):
    count=0
    for i,coord in enumerate(bishops):
        x,y=coord
        print("i:",i, coord)
        for j in range(0,i):
            x1,y1=bishops[j]
            if abs(x1-x) == abs(y1-y):
                count+=1
                print("j:",j, "count:", count)
    return count

assert count_attack_bishop_pairs(5, [ (0,0), (1,2), (2,2), (4,0) ])==2

