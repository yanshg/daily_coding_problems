#!/usr/bin/python

"""

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.

"""

# Idea:  use DFS
#
#        need check if one vertex has itself as its neighbor, so use 'parent' to identify

def search_dfs(graph,vertex,visited,parent):
    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if search_dfs(graph,neighbor,visited,vertex):
                return True
        elif neighbor!=parent:
            return True

    return False

def is_cycle_exist(graph):
    visited=set()
    for vertex in graph:
        if vertex not in visited:
            if search_dfs(graph,vertex,visited,None):
                return True
    return False


graph={
    'a': [ 'b', 'c' ],
    'b': [ 'd' ],
    'c': [ 'd' ],
    'd': [ 'a' ],
}
assert is_cycle_exist(graph)
