#!/usr/bin/python

"""

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.

"""


import heapq

def rearrange_string(string):
    counts=[ (-string.count(c),c) for c in set(string) ]
    heapq.heapify(counts)

    if any([-cnt>(len(string)+1)//2 for cnt,c in counts]):
        return None

    str=''
    while len(counts)>1:
        cnt1,ch1=heapq.heappop(counts)
        cnt2,ch2=heapq.heappop(counts)
        str+=ch1+ch2

        if cnt1+1<0: heapq.heappush(counts,(cnt1+1,ch1))
        if cnt2+1<0: heapq.heappush(counts,(cnt2+1,ch2))

    str+=counts[0][1] if counts else ''

    return str


assert rearrange_string("aaabbc")=="ababac"
assert not rearrange_string("aaab")

