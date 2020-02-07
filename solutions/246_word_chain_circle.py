#!/usr/bin/python

"""

This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair.

"""

# Idea: use FIRST character to build a graph, and run DFS on graph

from collections import defaultdict

def build_graph(words):
    graph=defaultdict(list)
    for word in words:
        first_char=word[0]
        graph[first_char].append(word)
    return graph

# Check if circle with DFS
def check_graph(graph,start,path=[],visited=set()):
    if start in visited:
        print("path: ",path+[start])
        return True

    visited.add(start)
    path+=[start]

    last_char=start[-1]
    for next in graph[last_char]:
        if check_graph(graph,next,path[:],visited):
           return True

    return False

def check_circle(words):
    graph=build_graph(words)
    for start in words:
        if check_graph(graph,start,[],set()):
            return True
    return False

assert check_circle(['chair', 'height', 'racket', 'touch', 'tunic'])
assert check_circle(['chair', 'height', 'racket', 'tunic'])
assert check_circle(['chair', 'racket', 'tunic'])
assert not check_circle(['chair', 'height', 'tunic'])
assert not check_circle(['chair', 'height', 'racket'])
