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

# From above description:
# 1. cons() return a function, and this function need an argument which should also be function
# 2. car() and cdr()'s argument should be a function, which require another function as argument


# Functions of Functions
#
# This is used to run different functions on same data with some same processing.
#
# like: BloomFilter to use different hash functions on same number
#       to get different hash value.
#
# Steps 1:
#
#        1. create general_function(function as argument),
#        2. general_function(func) return a function(data as argument): like
#
#   def general_function(sub_func):
#       def return_func(data):
#           result=sub_func(data)
#           return process(result)
#       return return_func
#
#        3. define sub functions as:
#
#   sub_funcs=[ func1, func2 ]
#   functions=[ general_function(func) for func in sub_funcs ]
#   values=[ func(data) for func in functions ]
#
#
# Steps 2:
#
#        1. create general_function(data as argument),
#        2. general_function(data) return a function(function as argument): like
#
#   def general_function(data):
#       def return_func(sub_func):
#           result=sub_func(data)
#           return process(result)
#       return return_func
#
#        3. define sub functions as:
#
#   def subfunc1(data):
#       gf=general_function(data)
#       return gf(func1)
#
#   def subfunc2(data):
#       gf=general_function(data)
#       return gf(func2)
#
#        4. call sub functions as:
#
#   v1=subfunc1(data)
#   v2=subfunc2(data)
#

# Solution with steps 1

def cons1(f):
    return lambda a,b: f(a,b)

def car1(a,b):
    f=cons1(lambda x,y:x)
    return f(a,b)

def cdr1(a,b):
    f=cons1(lambda x,y:y)
    return f(a,b)

assert car1(3, 4) == 3
assert cdr1(3, 4) == 4

# Solution with steps 2

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


