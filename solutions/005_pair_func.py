#!/usr/bin/python

"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

# from above description:
# 1. cons() return a function, and this function need an argument which should also be function
# 2. car() and cdr()'s argument should be a function, which require another function as argument

def cons(a,b):
    return lambda f: f(a,b)

def car(f):
    z=lambda x,y:x
    return f(z)

def cdr(f):
    z=lambda x,y:y
    return f(z)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
