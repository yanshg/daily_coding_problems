#!/usr/bin/python

"""

This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.

"""

from collections import defaultdict

class Node():
    def __init__(self,char):
        self.char=char
        self.edges=list()

    def __repr__(self):
        return "{}: {}".format(self.char,self.edges)

class Graph():
    def __init__(self,chars,edges=[]):
        self.chars=chars
        self.edges=edges
        self._initialize_nodes(chars)
        self._initialize_edges(edges)

    def _initialize_nodes(self,chars):
        self.nodes=[ Node(c) for c in chars ]

    def _initialize_edges(self,edges):
        for edge in edges:
            start,end=edge
            node=self.nodes[start]
            node.edges.append(edge)

    def __repr__(self):
        return "nodes: {}, edges: {}".format(self.nodes,self.edges)

    def _get_connected_nodes(self, node):
        return [ self.nodes[end] for start,end in node.edges ]

    def _get_path_value(self,path):
        pathvals=defaultdict(int)
        for p in path:
            pathvals[p]+=1
        return max(pathvals.values())

    # Idea:  Use dynamic programming
    #        1. the node is visited, return 0
    #        2. check each connected node
    def _get_largest_path(self,node,path=[],visited=set()):
        id_node=id(node)
        if id_node in visited:
            return 0

        path+=[node.char]
        visited.add(id_node)

        connected_nodes=self._get_connected_nodes(node)
        if not connected_nodes:
            print("path: ", path)
            return self._get_path_value(path)

        return max([ self._get_largest_path(node1,path[:],visited.copy()) for node1 in connected_nodes ])

    def get_largest_path(self):
        return max([ self._get_largest_path(node,[],set()) for node in self.nodes ])

g=Graph('ABACA',[(0,1),(0,2),(2,3),(3,4)])
print(g)
assert g.get_largest_path()==3

g=Graph('A',[(0,0)])
print(g)
assert g.get_largest_path()==0
