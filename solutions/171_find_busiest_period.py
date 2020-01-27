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

def find_busiest_period(entries):
    entries.sort(key=lambda x: x['timestamp'])

    max_ending_here,max_so_far=0,0
    max_pair=[0,0]

    for entrie in entries:
        count=entrie['count'] if entrie['type']=='enter' else -entrie['count']
        if max_ending_here + count > count:
            max_ending_here=max_ending_here + count
            if max_ending_here > max_so_far:
                max_so_far=max_ending_here
                max_pair[1]=entrie['timestamp']
        else:
            max_ending_here=count
            max_pair[0]=max_pair[1]=entrie['timestamp']


    return max_pair

entries = [
            {"timestamp": 1526579928, 'count': 3, "type": "enter"},
            {"timestamp": 1526580382, 'count': 2, "type": "exit"},
            {"timestamp": 1526580400, 'count': 5, "type": "enter"},
]

assert find_busiest_period(entries) == [ 1526579928, 1526580400 ]

entries = [
            {"timestamp": 1526579928, "count": 3, "type": "enter"},
            {"timestamp": 1526579982, "count": 4, "type": "enter"},
            {"timestamp": 1526580054, "count": 5, "type": "exit"},
            {"timestamp": 1526580128, "count": 1, "type": "enter"},
            {"timestamp": 1526580382, "count": 3, "type": "exit"}
]
assert find_busiest_period(entries) == (1526579982, 1526580054)
