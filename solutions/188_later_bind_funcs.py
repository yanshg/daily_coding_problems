#!/usr/bin/python

"""

This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

How can we make it print out what we apparently want?

"""

# print "3 3 3"

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i=i):
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

