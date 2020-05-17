#!/usr/bin/python

"""

This problem was asked by Uber.

On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

"""

import heapq
from collections import defaultdict

class FraudVoteException(Exception):
    pass

def get_votes_from_file(file):
    votes=[]
    with open(file,'r') as fh:
        data=fh.readlines()
        for line in data:
            voter,candidate=line.split()
            votes+=[(voter,candidate)]
    return votes

def process_votes(votes):
    error_votes=[]
    voters=set()
    candidates_votes=defaultdict(int)
    for voter,candidate in votes:
        if voter in voters:
            error_votes+=[(voter,candidate)]
        else:
            voters.add(voter)
            candidates_votes[candidate]+=1

    if error_votes:
        print("error votes: ",error_votes)
        raise FraudVoteException

    return candidates_votes

def get_top_candidates(candidates_votes):
    freqs=[]
    for candidate,freq in candidates_votes.items():
        heapq.heappush(freqs,(freq,candidate))

    tops=[ top[1] for top in freqs[-3:] ]
    print("tops: ", tops)
    return tops

def get_tops_from_file(file):
    return get_top_candidates(process_votes(get_votes_from_file(file)))

def get_tops_from_votes(votes):
    return get_top_candidates(process_votes(votes))

if __name__ == '__main__':
    votes=[
        ('v1','c1'),
        ('v2','c2'),
        ('v3','c2'),
        ('v4','c2'),
        ('v5','c1'),
        ('v6','c3'),
        ('v7','c3'),
        ('v8','c4'),
        ('v9','c3'),
    ]

    file='/tmp/votes.txt'
    with open(file,'w') as fh:
        for v,c in votes:
            fh.write(v+' '+c+'\n')

    assert get_tops_from_file(file)==['c1','c2','c3']
    assert get_tops_from_votes(votes)==['c1','c2','c3']

