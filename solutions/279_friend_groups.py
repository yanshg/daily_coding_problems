#!/usr/bin/python

"""

This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.

"""

# Idea: Disjoint-set data structure, use union and find

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sizes = [1] * n
        self.count = n

    def union(self,p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return

        if self.sizes[rootp] > self.sizes[rootq]:
            rootp,rootq = rootq,rootp

        self.parent[rootp] = rootq
        self.sizes[rootq] += self.sizes[rootp]
        self.count -= 1

    def find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def get_count(self):
        return self.count

def get_friend_groups(students):
    ds = DisjointSet(len(students))
    for student,friends in students.items():
        for friend in friends:
            ds.union(student,friend)

    return ds.get_count()

students={ 0: [1, 2],
           1: [0, 5],
           2: [0],
           3: [6],
           4: [],
           5: [1],
           6: [3]}

assert get_friend_groups(students) == 3
