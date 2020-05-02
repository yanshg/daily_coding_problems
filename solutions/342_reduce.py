#!/usr/bin/python

"""

This problem was asked by Stripe.

reduce (also known as fold) is a function that takes in an array, a combining function, and an initial value and builds up a result by calling the combining function on each element of the array, left to right. For example, we can write sum() in terms of reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array, and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.

"""

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def reduce_recursion(lst, f, init):
    if not lst:
        return init

    return reduce(lst[1:], f, f(init,lst[0]))

def reduce(lst, f, init):
    result=init
    for i in lst:
        result=f(result, i)
    return result

def rsum(lst):
    return reduce(lst,add,0)

def rprod(lst):
    return reduce(lst,multiply,1)

assert rsum([1,2,3])==6
assert rprod([1,2,3])==6
