#!/usr/bin/python

"""

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

"""

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[ [ 0 for col in range(vertices)] for row in range(vertices) ]
        self.colors= []

    def can_color(self, k):
        if len(self.colors)==self.vertices:
            print("colors: ", self.colors)
            return True

        for color in range(1,k+1):
            if self.is_valid_color(color):
                self.colors.append(color)
                if self.can_color(k):
                    return True
                self.colors.pop()

        return False

    def is_valid_color(self, color):
        vertex=len(self.colors)
        for v,connected in enumerate(self.graph[vertex]):
             if v<vertex and connected and self.colors[v]==color:
                 return False

        return True

graph=Graph(4)
graph.graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]

graph.colors=[]
assert graph.can_color(4)

graph.colors=[]
assert not graph.can_color(3)

graph=Graph(4)
graph.graph = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

graph.colors=[]
assert graph.can_color(4)

graph.colors=[]
assert graph.can_color(1)

graph=Graph(4)
graph.graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]

graph.colors=[]
assert graph.can_color(4)

graph.colors=[]
assert graph.can_color(3)

graph.colors=[]
assert graph.can_color(2)

graph.colors=[]
assert not graph.can_color(1)
