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

from collections import defaultdict

GROUP1=1
GROUP2=2
GROUP_ERROR=3

def get_group(groups,students):
    group=0
    for student in students:
        group1=groups[student]
        if group1:
            if group and group1!=group:
                return GROUP_ERROR
            group=group1
    return GROUP1 if not group or group==GROUP2 else GROUP2

# DFS
def helper(students,student,groups):
    enemies=students[student]
    groups[student]=get_group(groups,enemies)
    for enemy in enemies:
        if not groups[enemy]:
            if groups[student]==GROUP_ERROR:
                groups[enemy]=GROUP_ERROR
            else:
                groups[enemy]=GROUP1 if groups[student]==GROUP2 else GROUP2
            helper(students,enemy,groups)

def get_groups(students):
    groups=defaultdict(int)
    for student in students:
        if not groups[student]:
            helper(students,student,groups)

    #print("groups:",groups)
    group_error={student for student in groups if groups[student]==GROUP_ERROR}
    if group_error:
        return None

    group1={student for student in groups if groups[student]==GROUP1}
    group2={student for student in groups if groups[student]==GROUP2}
    #print("group1:",group1, "group2:",group2)
    return [group1,group2]

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

assert get_groups(students)==[{0, 1, 4, 5}, {2, 3}]

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

assert not get_groups(students)

