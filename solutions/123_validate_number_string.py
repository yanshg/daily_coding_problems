#!/usr/bin/python

"""
This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"
"""

def is_valid_num_with_try(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

import re
def is_valid_num_with_re(string):
    mo=re.match(r'[+-]?\d*\.?\d+([eE][+-]?\d+)?$',string)
    return bool(mo)

assert is_valid_num_with_try("1e5")
assert is_valid_num_with_re("1e5")

assert is_valid_num_with_try("10")
assert is_valid_num_with_try("-10")
assert is_valid_num_with_try("10.1")
assert is_valid_num_with_try("-10.1")
assert is_valid_num_with_try("1e5")
assert not is_valid_num_with_try("x 1")
assert not is_valid_num_with_try("a -1")
assert not is_valid_num_with_try("-")

assert is_valid_num_with_re("10")
assert is_valid_num_with_re("-10")
assert is_valid_num_with_re("10.1")
assert is_valid_num_with_re("-10.1")
assert is_valid_num_with_re("1e5")
assert not is_valid_num_with_re("x 1")
assert not is_valid_num_with_re("a -1")
assert not is_valid_num_with_re("-")
