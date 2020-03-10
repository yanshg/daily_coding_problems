#!/usr/bin/python

"""

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.

"""

# Idea:  use DFS

class Node:
    def __init__(self,val):
        self.val=val
        self.adj_nodes=[]
        
class Graph:
    def __init__(self, vertex, edges):
        self.vertex=vertex
        self.edges=edges

    def is_cycle_exists(self):
        return False


def dfs_helper(graph,start,visited=set()):
    if start in visisted:
        return True

    visited.add(start)

    for next in graph[start]:
        if dfs_helper(graph,next,visited)
            return True

    return False

def is_cycle_exist(gragh):
    for start in graph:
        if dfs_helper(graph,start,set()):
            return True
    return False


gragh={
    'a': [ 'b', 'c' ],
    'b': [ 'd' ],
    'c': [ 'd' ],
    'd': [ 'a' ],
}
assert is_cycle_exist(gragh)
