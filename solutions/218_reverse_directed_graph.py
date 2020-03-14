#!/usr/bin/python

"""

This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C.

"""

# DFS

def graph_dfs(graph,new_graph,start,visited=set()):
    if start in visited:
        return

    visited.add(start)
    for node in graph[start]:
        new_graph[node]+=[start]
        graph_dfs(graph,new_graph,node,visited)

def revert_graph(graph):
    # Initialize new graph
    new_graph=dict()
    for node in graph:
        new_graph[node]=[]

    # DFS
    visited=set()
    for node in graph:
        graph_dfs(graph,new_graph,node,visited)

    return new_graph

graph={ 'A': [ 'B' ], 'B': [ 'C'], 'C':[] }
assert revert_graph(graph)=={'C': [ 'B' ], 'B': ['A'], 'A':[]}

