#!/usr/bin/python

"""

This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.

"""

# Article: https://www.geeksforgeeks.org/bipartite-graph/

# Idea:    1. Assign RED color to the source vertex (putting into set U).
#          2. Color all the neighbors with BLUE color (putting into set V).
#          3. Color all neighbor's neighbor with RED color (putting into set U).
#          4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m=2.
#          5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)

# Use DFS

def bipartite_check_helper(graph,vertex,visited,parent_set):
    visited[vertex]=parent_set

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if not bipartite_check_helper(graph,neighbor,visited,1-parent_set):
                return False
        elif visited[neighbor]==parent_set:
                return False
    return True

def is_bipartite_graph(graph):
    visited=dict()
    for vertex in graph:
        if vertex not in visited:
            if not bipartite_check_helper(graph,vertex,visited,0):
                return False
    return True

graph={
    'a': [ 'b' ],
    'b': [ 'c' ],
    'c': [ 'd' ],
    'd': [ 'e' ],
    'e': [ 'a' ],
}
assert not is_bipartite_graph(graph)

graph={
    'a': [ 'b' ],
    'b': [ 'c' ],
    'c': [ 'd' ],
    'd': [ 'e' ],
    'e': [ 'f' ],
    'f': [ 'a' ],
}
assert is_bipartite_graph(graph)
