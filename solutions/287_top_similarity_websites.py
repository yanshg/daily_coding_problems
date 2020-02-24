#!/usr/bin/python

"""

This problem was asked by Quora.

You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].

"""

import heapq
from collections import defaultdict

def compute_similarity(visitors,site1,site2):
    return float(len(visitors[site1]&visitors[site2]))/len(visitors[site1]|visitors[site2])

def top_pairs(logs,k):
    visitors=defaultdict(set)
    for site,user in logs:
        visitors[site].add(user)

    sites=list(visitors.keys())
    n=len(sites)

    pairs=[]
    for i in range(k):
        heapq.heappush(pairs,(0,('','')))

    for i in range(n-1):
        for j in range(i+1,n):
            site1,site2=sites[i],sites[j]
            score=compute_similarity(visitors,site1,site2)
            heapq.heappushpop(pairs,(score, (site1,site2)))

    return [pair[1] for pair in pairs]

logs=[('a', 1), ('a', 3), ('a', 5),
      ('b', 2), ('b', 6),
      ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
      ('d', 4), ('d', 5), ('d', 6), ('d', 7),
      ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

assert top_pairs(logs,1)==[('a','e')]
