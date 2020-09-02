#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

"""

from collections import defaultdict
import random

NUM_CARDS=5

def shuffle_cards(cards):
    n=len(cards)
    for i in range(n-1):
        index = random.randint(i, n-1)
        cards[i], cards[index] = cards[index], cards[i]

    return cards


num_experiments = 10000
count = defaultdict(int)

cards=list(range(NUM_CARDS))
for i in range(num_experiments):
    shuffle_cards(cards)
    print(cards)
    count[tuple(cards)]+=1

print(count)
