#!/usr/bin/python

"""

This problem was asked by Adobe.

You are given a tree with an even number of nodes. Consider each connection between a parent and child node to be an "edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:

   1
  / \
 2   3
    / \
   4   5
 / | \
6  7  8

In this case, removing the edge (3, 4) satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.

"""

# DFS
from collections import defaultdict

def traverse(graph,curr,visited,counts):
    visited.add(curr)

    count=1
    children=graph[curr] if curr in graph else []
    for child in children:
        if child not in visited:
            count+=traverse(graph,child,visited,counts)

    counts[curr]=count
    return count

def get_max_removable_edges(graph,start):
    visited=set()
    counts=defaultdict(int)
    traverse(graph,start,visited,counts)

    if counts[start]%2==1:
        return 0
    return len([ 1 for val in counts.values() if val%2==0 ])-1

graph={
    '1': [ '2', '3' ],
    '3': [ '4', '5' ],
    '4': [ '6', '7', '8' ],
}
assert get_max_removable_edges(graph,'1')==2

