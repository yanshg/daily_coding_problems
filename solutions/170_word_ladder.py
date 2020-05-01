#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.

"""

# Bidirectional BFS

from collections import deque

def is_adjacent(w1,w2):
    if w1==w2 or len(w1)!=len(w2):
        return False
    return (sum([ 1 for i in range(len(w1)) if w1[i]!=w2[i] ]))==1

# Get graph
def build_graph(start,words):
    graph=dict()

    # Note: use | to union sets, instead of +
    for w1 in {start}|words:
        graph[w1]=[ w2 for w2 in words if is_adjacent(w1,w2) ]

    return graph

# BFS:
def word_ladder_bfs(start,end,words):
    if end not in words:
        return None

    graph=build_graph(start,words)
    print("graph:",graph)

    visited=set()
    dq=deque([(start,[start])])

    while dq:
        (word,path)=dq.popleft()
        if word==end:
            return path

        visited.add(word)
        for w in graph[word]:
            if w not in visited:
                dq.append((w,path+[w]))

    return None

# Bidirectional BFS
def word_ladder_bi_bfs(start,end,words):
    if end not in words:
        return None

    graph=build_graph(start,words)

    fwd_visited=set()
    fwd_dq=deque([(start,[start])])

    bwd_visited=set()
    bwd_dq=deque([(end,[end])])

    while fwd_dq and bwd_dq:
        (word1,path1)=fwd_dq.popleft()
        fwd_visited.add(word1)

        (word2,path2)=bwd_dq.popleft()
        bwd_visited.add(word2)

        visited_this_level=set()

        for w in graph[word1]:
            if w == word2:
                # Found intersection:
                return path1+[w]+list(reversed(path2))
            elif w not in fwd_visited:
                fwd_dq.append((w,path1+[w]))
                visited_this_level.add(w)

        for w in graph[word2]:
            if w == word1 or w in visited_this_level:
                # Found intersection
                return path1+[w]+list(reversed(path2))
            elif w not in bwd_visited:
                bwd_dq.append((w,path2+[w]))

    return None

assert word_ladder_bfs('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert not word_ladder_bfs('dog','cat',{"dot", "tod", "dat", "dar"})
assert word_ladder_bi_bfs('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert not word_ladder_bi_bfs('dog','cat',{"dot", "tod", "dat", "dar"})

