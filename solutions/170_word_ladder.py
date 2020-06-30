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
    if w1 == w2 or len(w1) != len(w2):
        return False
    return sum([ c1 != c2 for c1,c2 in zip(w1,w2) ])==1

# Build graph
def build_graph(start,words):
    graph = dict()

    # Note: use | to union sets, instead of +
    for w1 in {start} | words:
        graph[w1] = [ w2 for w2 in words if is_adjacent(w1,w2) ]

    return graph

# BFS:
def word_ladder_bfs(start,end,words):
    if end not in words:
        return None

    graph = build_graph(start,words)
    print("graph:",graph)

    visited = set()
    dq = deque([(start,[start])])

    while dq:
        (word,path) = dq.popleft()
        #print(path)
        if word == end:
            return path

        visited.add(word)
        for w in graph[word]:
            if w not in visited:
                dq.append((w,path+[w]))

    return None

# Bidirectional BFS
#
# Articles: https://leetcode.com/articles/word-ladder/#
#           https://blog.csdn.net/ZouCharming/article/details/90757577

# Idea:  1. set q1 from start point,
#        2. set q2 from end point.
#        3. set the shorter queue as q1, longer as q2,
#        4. get all adjacent words of each word in q1, and set it to q3
#        5. if any word in q3 can be found in q2, it is the cross point, return the path
#        6. q1=q3
#        7. loop from #3

def word_ladder_bibfs(start,end,words):
    if end not in words:
        return None

    graph = build_graph(start,words)

    q1 = { start: [start] }
    q2 = { end:   [end] }

    is_q1_start = True
    visited = set()

    while q1 and q2:
        if len(q1)>len(q2):
            q1,q2 = q2, q1
            is_q1_start = not is_q1_start

        q3 = dict()

        for word,path in q1.items():
            if word in q2:
                # find cross word
                if is_q1_start:
                    full_path=path[:-1] + list(reversed(q2[word]))
                else:
                    full_path=q2[word] + list(reversed(path[:-1]))
                return full_path

            visited.add(word)

            for adj_word in graph[word]:
                if adj_word not in visited and  \
                   adj_word not in q3:
                    q3[adj_word]=path+[adj_word]

        q1=q3

    return None

assert word_ladder_bfs('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert not word_ladder_bfs('dog','cat',{"dot", "tod", "dat", "dar"})
assert word_ladder_bibfs('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert not word_ladder_bibfs('dog','cat',{"dot", "tod", "dat", "dar"})
