#!/usr/bin/python

"""

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

def get_min_rooms(intervals):
    # status: 1 mean room occupied, -1 mean room released
    start_times=[ (t[0],1) for t in intervals ]
    end_times=[ (t[1],-1) for t in intervals ]
    status=[ t[1] for t in sorted(start_times+end_times, key=lambda t: t[0]) ]

    rooms,max_rooms=0,0
    for event in status:
        rooms+=event
        max_rooms=max(rooms,max_rooms)

    return max_rooms

assert get_min_rooms([(30, 75), (0, 50), (60, 150)])==2
