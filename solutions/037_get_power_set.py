#!/usr/bin/python

"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

# Idea: P(S) = P(S-a0) + { (a0 | Pi) for Pi in P(S-a0) }

def get_power_set(arr):
    if len(arr)==0:
        return [set()]

    sub_power_set = get_power_set(arr[1:])
    return sub_power_set + [ ({arr[0]} | s) for s in sub_power_set ]

assert get_power_set([]) == [set()]
assert get_power_set([1]) == [set(), {1}]
assert get_power_set([1, 2]) == [set(), {2}, {1}, {1, 2}]
assert get_power_set([1, 2, 3]) == [set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]
