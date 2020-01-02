#!/usr/bin/python

"""

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

"""

def faster_pow(x, y):
    #print("x: ",x, "y: ", y)
    if x==0:
        return 0

    if y==0:
        return 1
    elif y==1:
        return x
    else:
        return faster_pow(x*x, y//2) * faster_pow(x, y%2)

assert faster_pow(2, 10)==1024
