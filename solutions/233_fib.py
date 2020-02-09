#!/usr/bin/python

"""

This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

"""

def fib(n):
    a,b=0,1
    if n==0:
        return 0
    for i in range(1,n):
        a,b=b,a+b
    return b

assert fib(0)==0
assert fib(1)==1
assert fib(2)==1
assert fib(3)==2
assert fib(4)==3
assert fib(5)==5
assert fib(6)==8


