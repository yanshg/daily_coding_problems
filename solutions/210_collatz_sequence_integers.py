#!/usr/bin/python

"""

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

 * if n is even, the next number in the sequence is n / 2
 * if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""

# Idea: need use memo
#        |- [1]             if n==1
# f(n) = |- [n] + f(n//2)   if n is even
#        |- [n] + f(3*n+1)  if n is odd


def get_collatz_seq(n,memo=dict()):
    if n==1:
        return [ 1 ]

    if n in memo:
        return memo[n]

    if n&1:
        memo[n] = [n] + get_collatz_seq(3*n+1,memo)
    else:
        memo[n] = [n] + get_collatz_seq(n//2,memo)

    return memo[n]

def get_longest_collatz_seq(n):
    memo=dict()
    longest=[]
    for i in range(1,n+1):
        seq=get_collatz_seq(i,memo)
        print(i,": ", seq)
        if len(seq)>len(longest):
            longest=seq
    return longest

print("1000 longest: ", get_longest_collatz_seq(1000))

