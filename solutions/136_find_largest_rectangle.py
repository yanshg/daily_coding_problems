#!/usr/bin/python

"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
"""

# Dynamic Programming method (Devide/Conquer/Combine)
#
# 1. breaking down an optimisation problem into smaller sub-problems
# 2. determine the relationship between the parent problem and sub problems
# 3. take care the end condition

# Optimisation problems seek the maximum or minimum solution.
# The general rule is that if you encounter a problem where the initial algorithm is solved in O(2n) time, it is better solved using Dynamic Programming.

# There are 3 main parts to divide and conquer:

# 1. Divide the problem into smaller sub-problems of the same type.
# 2. Conquer - solve the sub-problems recursively.
# 3. Combine - Combine all the sub-problems to create a solution to the original problem.

def extendable_row(matrix,erow,scol,ecol):
    return all(matrix[erow][scol:ecol])

def extendable_col(matrix,ecol,srow,erow):
    for row in range(srow,erow):
        if not matrix[row][ecol]:
            return False
    return True


def area_helper(matrix,rows,cols,srow,scol,erow,ecol):
    curr_area=(erow-srow) * (ecol-scol)

    ex_col_area,ex_row_area=0,0

    if erow<rows and extendable_row(matrix,erow,scol,ecol):
        ex_row_area=area_helper(matrix,rows,cols,srow,scol,erow+1,ecol)

    if ecol<cols and extendable_col(matrix,ecol,srow,erow):
        ex_col_area=area_helper(matrix,rows,cols,srow,scol,erow,ecol+1)

    return max(curr_area, ex_col_area, ex_row_area)

def get_largest_area(matrix):
    max_area=0
    if not matrix:
        return max_area

    rows,cols=len(matrix),len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            upper_max_area=(rows-i) * (cols-j)
            if matrix[i][j] and upper_max_area>max_area:
                area=area_helper(matrix,rows,cols,i,j,i+1,j+1)
                max_area=max(area, max_area)

    return max_area

# Tests

matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 0]]

assert get_largest_area(matrix) == 4
