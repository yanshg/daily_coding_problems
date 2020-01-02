#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

"""

from collections import defaultdict,Counter
import random

NUM_CARDS=52

def generate_random_number(k):
    return random.randint(1,k)

def shuffle_cards(cards):
    #random.shuffle(cards)

    n=len(cards)
    for i in range (0, n-2):
        index = i + generate_random_number(n-i-1)
        cards[i], cards[index] = cards[index], cards[i]

    return cards


num_experiments = 10
count = defaultdict(int)

cards=list(range(NUM_CARDS))
for i in range(num_experiments):
    shuffle_cards(cards)
    print(cards)
    count[tuple(cards)]+=1

print(len(count), Counter(count.values()))
