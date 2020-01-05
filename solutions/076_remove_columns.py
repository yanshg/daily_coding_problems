#!/usr/bin/python

"""

This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.

"""

# O(M * NlogN)
def bruteforce(matrix):
    if not matrix or len(matrix)==1:
        return 0

    # Note: python3 zip() returns an iterator which yields tuples on demand and can be traversed only once

    # Use zip() to get columns, and sort them with tuple format, them compare
    cols=list(zip(*matrix))
    sorted_cols=list(map(lambda x:tuple(sorted(x)), cols))
    #print("cols: ", cols, "sorted_cols: ", sorted_cols)

    return sum([ 1 if cols[i]!=sorted_cols[i] else 0 for i in range(len(cols)) ])


# O(M * N)
def get_removal_columns(matrix):
    if not matrix or len(matrix)==1:
        return 0

    # If the items do not have same length,
    # then need use itertools.zip_longest(*matrix,fillvalue='') to get columns

    count=0
    for col in zip(*matrix):
        #print("col: ", col)
        for i in range(len(col)-1):
            if col[i]>col[i+1]:
                count+=1
                break

    return count

assert bruteforce(["abcdef"]) == 0
assert bruteforce(["cba", "daf", "ghi"]) == 1
assert bruteforce(["zyx", "wvu", "tsr"]) == 3

assert get_removal_columns(["abcdef"]) == 0
assert get_removal_columns(["cba", "daf", "ghi"]) == 1
assert get_removal_columns(["zyx", "wvu", "tsr"]) == 3
