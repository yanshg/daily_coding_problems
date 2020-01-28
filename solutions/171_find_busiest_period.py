#!/usr/bin/python

"""
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""

# Idea:  it is mostly same to the 049 problem which to find maximum sum of any contiguous subarray of the array

def find_busiest_period(entries):
    entries.sort(key=lambda x: x['timestamp'])

    max_ending_here,max_so_far=0,float('-inf')
    max_period=[0,0]
    new_max_period=False

    for entrie in entries:
        count=entrie['count'] if entrie['type']=='enter' else -entrie['count']
        max_ending_here=max(max_ending_here + count, count)

        if max_ending_here > max_so_far:
            # Got a new max, re-set the max period
            max_so_far=max_ending_here
            max_period[0]=max_period[1]=entrie['timestamp']
            new_max_period=True
        elif new_max_period:
            # Need set the end value for the previos max period.
            max_period[1]=entrie['timestamp']
            new_max_period=False

    return max_period

entries = [
            {"timestamp": 1526579928, 'count': 3, "type": "enter"},
            {"timestamp": 1526580382, 'count': 2, "type": "exit"},
            {"timestamp": 1526580400, 'count': 5, "type": "enter"},
]

assert find_busiest_period(entries) == [ 1526580400, 1526580400 ]

entries = [
            {"timestamp": 1526579928, "count": 3, "type": "enter"},
            {"timestamp": 1526579982, "count": 4, "type": "enter"},
            {"timestamp": 1526580054, "count": 5, "type": "exit"},
            {"timestamp": 1526580128, "count": 1, "type": "enter"},
            {"timestamp": 1526580382, "count": 3, "type": "exit"}
]
assert find_busiest_period(entries) == [1526579982, 1526580054]
