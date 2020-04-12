#!/usr/bin/python

"""

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

 * if n is even, the next number in the sequence is n / 2
 * if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""

# Idea: need use cache

def next_collatz(n):
    if n&1:
        return 3*n+1
    return n//2

def get_collatz_seq(n,cache=dict()):
    if n==1:
        return [ 1 ]

    seq=[n]
    next_val=next_collatz(n)
    if next_val in cache:
        seq+=cache[next_val]
    else:
        seq+=get_collatz_seq(next_val,cache)
    cache[n]=seq
    return seq

def get_longest_collatz_seq(n):
    cache=dict()
    longest=[]
    for i in range(1,n+1):
        seq=get_collatz_seq(i,cache)
        if len(seq)>len(longest):
            longest=seq
    print(longest)
    return longest

get_longest_collatz_seq(1000)

