#!/usr/bin/python

"""
This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.

"""


# Idea: If G is an undirected graph, it's a standard lemma that the following are equivalent:
#       * G is a tree.
#       * G is connected and has no cycles.
#       * G is connected and the number of edges is one less than the number of vertices.
#
# So this is same with problem #280 to check if the graph is connected and has no cycles.

def graph_has_cycle(graph,vertex,visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in visited or graph_has_cycle(graph,neighbor,visited):
            return True
    return False

def is_minimal_connected_graph(graph):
    visited=set()
    checked=False
    for vertex in graph:
        if vertex not in visited:
            if checked or graph_has_cycle(graph,vertex,visited):
                checked=True
                return False
    return True

graph={
    'a': [ 'b', 'c' ],
    'b': [ 'd', 'e' ],
    'c': [ 'f' ],
    'd': [ ],
    'e': [ ],
    'f': [ ],
}
assert is_minimal_connected_graph(graph)

graph={
    'a': [ 'b' ],
    'b': [ 'c' ],
    'c': [ 'd' ],
    'd': [ 'e' ],
    'e': [ 'a' ],
}
assert not is_minimal_connected_graph(graph)

