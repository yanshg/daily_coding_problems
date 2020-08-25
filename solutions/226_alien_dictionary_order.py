#!/usr/bin/python

"""

This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].

"""

# Idea:  build a directed graph, then BFS to get the longest path

from collections import defaultdict

def alien_order(words):
    pre = defaultdict(set)
    suc = defaultdict(set)

    for w1,w2 in zip(words, words[1:]):
        for a,b in zip(w1,w2):
            # get first different character
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                break

    chars = set(''.join(words))

    todo = chars - set(pre)
    order = []
    while todo:
        c = todo.pop()
        order += [c]
        for s in suc[c]:
            pre[s].discard(c)
            if not pre[s]:
                todo.add(s)

    return order * (set(order) == chars)

assert alien_order(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'])==['x', 'z', 'w', 'y']
