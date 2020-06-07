#!/usr/bin/python

"""

This problem was asked by Yahoo.

You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string 'daily' and k = 1. The best we can create in this case is 'ailyd'.

"""

# if k==1, then it could be to find the minimum letter.
# if k>1,  then it just to sort the string.
#          for example: k=2, and string 'x1,x2,x3,x4,b,x5,x6,c,a'.
#          1.  first always take first letter to get 'a,x1,x2,x3,x4,b,x5,x6,c'
#          2.  then always take second letter to get 'a,b,x5,x6,c,x1,x2,x3,x4'
#          3.  then get 'x6,c,x1,x2,x3,x4,a,b,x5'
#          4.  then get 'x6,x1,x2,x3,x4,a,b,x5,c'
#          5.  then get 'x5,c,x6,x1,x2,x3,x4,a,b'
#          6.  then get 'x5,x6,x1,x2,x3,x4,a,b,c'
#          7.  then get 'a,b,c,x5,x6,x1,x2,x3,x4'

def get_smallest_string(s,k):
    if k>1:
        return ''.join(sorted(s))
    if k==1:
        min_i,min_c=0,s[0]
        for i,c in enumerate(s):
            if c<min_c:
                min_i,min_c=i,c
        return s[min_i:]+s[:min_i]

assert get_smallest_string('daily',1)=='ailyd'
assert get_smallest_string('daily',2)=='adily'
