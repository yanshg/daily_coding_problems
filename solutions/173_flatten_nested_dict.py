#!/usr/bin/python

"""
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

def flatten_dict(d,key_so_far=""):
    if d and isinstance(d,dict):
        if key_so_far:
            key_so_far+='.'
        for k in d:
            yield from flatten_dict(d[k], key_so_far+str(k))
    elif d:
        yield key_so_far,d
    elif not key_so_far:
        return {}

d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

flat_d = {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

assert dict(flatten_dict(d,'')) == flat_d
assert dict(flatten_dict({},'')) == {}
