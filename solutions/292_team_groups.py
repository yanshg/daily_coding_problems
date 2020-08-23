#!/usr/bin/python

"""

This problem was asked by Twitter.

A teacher must divide a class of students into two teams to play dodgeball. Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

On the other hand, given the input below, you should return False.

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}


"""

# https://www.geeksforgeeks.org/bipartite-graph/

# Check whether a graph is Bipartite by using 2-colors
#
# similiar with 207_bipartite_graph.py

# DFS
def bipartite_groups_dfs(students,student,group_set,visited):
    visited[student] = group_set

    enemy_set = 1-group_set
    for enemy in students[student]:
        if enemy not in visited:
            if not bipartite_groups_dfs(students,enemy,enemy_set,visited):
                return False
        elif visited[enemy] != enemy_set:
            return False

    return True

def get_groups_dfs(students):
    visited = dict()
    for student in students:
        if student not in visited:
            if not bipartite_groups_dfs(students,student,0,visited):
                return None

    return [ { s for s in visited if visited[s]==0 },
             { s for s in visited if visited[s]==1 } ]

# BFS
from collections import deque
def bipartite_groups_bfs(students,student,group_set,visited):
    dq = deque([(student,0)])
    while dq:
        s,group_set = dq.popleft()
        visited[s] = group_set

        enemy_set = 1-group_set

        for enemy in students[s]:
            if enemy not in visited:
                dq.append((enemy,enemy_set))
            elif visited[enemy] != enemy_set:
                return False

    return True

def get_groups_bfs(students):
    visited = dict()
    for student in students:
        if student not in visited:
            if not bipartite_groups_bfs(students,student,0,visited):
                return None

    return [ {s for s in students if visited[s]==0 },
             {s for s in students if visited[s]==1 } ]

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

assert get_groups_dfs(students)==[{0, 1, 4, 5}, {2, 3}]
assert get_groups_bfs(students)==[{0, 1, 4, 5}, {2, 3}]

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

assert not get_groups_dfs(students)
assert not get_groups_bfs(students)

