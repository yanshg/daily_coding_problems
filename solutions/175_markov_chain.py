#!/usr/bin/python

"""
This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

"""

import random,bisect
from collections import defaultdict

def get_transition_map(probabilities):
    trans_map=dict()
    for source,target,prob in probabilities:
        if source not in trans_map:
            trans_map[source]=([],[])

        next_states,probs=trans_map[source]
        next_states.append(target)
        prev_prob=0 if not probs else probs[-1]
        probs.append(prev_prob+prob)

    return trans_map

def get_next_state(trans_map,source,prob):
    if source not in trans_map:
        return source

    next_states,probs=trans_map[source]
    index=bisect.bisect(probs,prob)
    return next_states[index]

def run_markov_chain(probabilities,start,steps):
    trans_map=get_transition_map(probabilities)

    results=defaultdict(int)

    state=start
    results[state]+=1

    for i in range(steps):
        state=get_next_state(trans_map,state,random.random())
        results[state]+=1

    return results

probabilities=[ ('a', 'a', 0.9),
                ('a', 'b', 0.075),
                ('a', 'c', 0.025),
                ('b', 'a', 0.15),
                ('b', 'b', 0.8),
                ('b', 'c', 0.05),
                ('c', 'a', 0.25),
                ('c', 'b', 0.25),
                ('c', 'c', 0.5)
]

results=run_markov_chain(probabilities,'a',5000)
print(results)
assert results['a']>results['b']>results['c']
