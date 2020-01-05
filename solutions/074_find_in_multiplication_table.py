#!/usr/bin/python

"""

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.

"""

# Idea: simple but need take more attentions on test cases

# O(X^1/2)
def find_number_in_multiplication_table(n,x):
    if not n:
        return 0

    if n==1:
        return int(x==1)

    count,i=0,2
    while i<=n and i*i<=x:
        if x%i==0:
            count+=2
        i+=1
    count+=(x<n)*2
    return count

assert find_number_in_multiplication_table(0,1)==0
assert find_number_in_multiplication_table(1,1)==1
assert find_number_in_multiplication_table(1,12)==0
assert find_number_in_multiplication_table(6,12)==4
assert find_number_in_multiplication_table(6,13)==0
assert find_number_in_multiplication_table(8,6)==4
assert find_number_in_multiplication_table(3,2)==2
