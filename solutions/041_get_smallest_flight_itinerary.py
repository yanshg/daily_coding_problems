#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

"""

def get_itinerary(flights,start,itinerary=[]):
    #print("flights:", flights, "itinerary:", itinerary)
    if not flights:
        return itinerary+[start] if itinerary else None

    smallest_itinerary=None
    for i,(s,e) in enumerate(flights):
        if s==start:
            child_itinerary=get_itinerary(flights[:i]+flights[i+1:],e,itinerary+[s])
            if child_itinerary and \
                    (not smallest_itinerary or child_itinerary<smallest_itinerary):
                smallest_itinerary=child_itinerary

    #print("smallest itinerary:", smallest_itinerary)
    return smallest_itinerary

assert get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')==['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert not get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')
assert get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],'A')==['A', 'B', 'C', 'A', 'C']
