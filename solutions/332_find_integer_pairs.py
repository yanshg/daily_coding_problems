#!/usr/bin/python

"""

This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

    a + b = M
    a XOR b = N

"""

def find_pairs(m,n):
    return [ (a,m-a) for a in range(1,m//2+1) if a^(m-a) == n ]

assert find_pairs(40,8)==[(16,24)]
