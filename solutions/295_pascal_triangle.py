#!/usr/bin/python

"""

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

    The first row consists of the number 1.
    For each subsequent row, each element is the sum of the numbers directly above it, on either side.

For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?

"""

def pascal_triangle(k):
    row=[1]*k
    for i in range(2,k):
        for j in range(i-1,0,-1):
            row[j]+=row[j-1]
    return row

# DP
def helper(k,row=None):
    assert k>0

    if k==1 or k==2:
        return row

    helper(k-1,row)
    for i in range(k-2,0,-1):
        row[i]+=row[i-1]
    return row

def pascal_triangle_dp(k):
    row=[1]*k
    return helper(k,row)

assert pascal_triangle(1)==[1]
assert pascal_triangle(2)==[1,1]
assert pascal_triangle(3)==[1,2,1]
assert pascal_triangle(4)==[1,3,3,1]
assert pascal_triangle(5)==[1,4,6,4,1]
assert pascal_triangle(6)==[1,5,10,10,5,1]

print(pascal_triangle(100))
print(pascal_triangle_dp(100))


