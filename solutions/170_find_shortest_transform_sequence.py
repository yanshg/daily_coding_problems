#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.

"""

from collections import deque

def words_distance(w1,w2):
    if w1==w2:
        return 0

    l1,l2=len(w1),len(w2)
    if l1>l2:
        l1,l2=l2,l1

    distance=l2-l1
    for i in range(l1):
        distance+=int(w1[i]!=w2[i])
    return distance

# Get graph
def get_mapping(start,words):
    dq=deque([start])
    mapping=dict()
    while dq:
        w=dq.popleft()
        trans=[]
        for word in words:
            if words_distance(w,word)==1:
                trans.append(word)
                if word not in dq and word not in mapping:
                    dq.append(word)

        mapping[w]=trans

    return mapping

# DFS on graph
def helper(start,end,mapping,path_so_far,all_paths):
    if start==end and path_so_far:
        all_paths.append(path_so_far)
    elif start in mapping:
        for word in mapping[start]:
            if word not in path_so_far:
                helper(word,end,mapping,path_so_far+[word],all_paths)

def find_shortest_transform_path(start,end,words):
    all_paths=[]
    mapping=get_mapping(start,words)
    print("mapping:", mapping)
    helper(start,end,mapping,[start],all_paths)
    if all_paths:
        print("all_paths: ", all_paths)
        return min(all_paths,key=len)
    return None

assert find_shortest_transform_path('dog','cat',{"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"];
assert find_shortest_transform_path('dog','cat',{"dot", "tod", "dat", "dar"}) == None

