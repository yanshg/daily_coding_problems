#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.

"""

def words_distance(w1,w2):
    if w1==w2:
        return 0

    l1,l2=len(w1),len(w2)
    l1,l2=(l1,l2) if l1<l2 else (l2,l1)

    distance=l2-l1
    for i in range(l1):
        distance+=int(w1[i]!=w2[i])
    return distance

# Get graph
def build_graph(start,words):
    graph=dict()
    all_words=words if start in words else [start]+list(words)
    for w1 in all_words:
        trans=[]
        for w2 in words:
            if words_distance(w1,w2)==1:
                trans.append(w2)
        graph[w1]=trans
    return graph

# DFS on graph
def helper(start,end,graph,path):
    if start==end:
        return path

    shortest_path=[]
    for word in graph[start]:
        if word not in path:
           sub_path=helper(word,end,graph,path+[word])
           if sub_path and \
                (not shortest_path or len(sub_path)<=len(shortest_path)):
               shortest_path=sub_path

    return shortest_path

def find_shortest_transform_path(start,end,words):
    graph=build_graph(start,words)
    print("graph:", graph)
    return helper(start,end,graph,[start])

assert find_shortest_transform_path('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert not find_shortest_transform_path('dog','cat',{"dot", "tod", "dat", "dar"})

