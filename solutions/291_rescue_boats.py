#!/usr/bin/python

"""

This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

"""

# O(NlogN)
def get_minimum_rescue_boats(weights,limit):
    weights.sort()

    boats=0
    low,high=0,len(weights)-1
    while low<=high:
        if low==high:
            low+=1
        elif weights[low]+weights[high]>limit:
            high-=1
        else:
            low+=1
            high-=1
        boats+=1

    return boats

assert get_minimum_rescue_boats([100, 200, 150, 80], 200)==3
assert get_minimum_rescue_boats([50, 80, 100, 120, 150, 200], 200)==4
