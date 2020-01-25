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

def flatten_dict_helper(d,flatten_dict,key_so_far=""):
    if not isinstance(d,dict):
        if key_so_far:
            flatten_dict[key_so_far]=d
        return flatten_dict

    for k in d:
        flatten_key="{}.{}".format(key_so_far,k) if key_so_far else k
        flatten_dict_helper(d[k],flatten_dict,flatten_key)

    return flatten_dict

def flatten_dict(d):
    return flatten_dict_helper(d,{},"")

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

assert flatten_dict(d) == flat_d
assert flatten_dict({}) == {}
