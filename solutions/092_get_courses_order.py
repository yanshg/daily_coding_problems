#!/usr/bin/python

"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

# Idea:  Topological sort on a graph
#
#        1. Build prereqs and successors
#        2. get list of cources without prereqs as independant courses
#        3. remove each independent courses from prereqs
#        4. retry #2 and #3

from collections import defaultdict

def toposort(courses_to_prereqs):
    # build graph
    pre=defaultdict(set)
    suc=defaultdict(set)
    for course,prereqs in courses_to_prereqs.items():
        for prereq in prereqs:
            pre[course].add(prereq)
            suc[prereq].add(course)

    # get indepedent courses
    courses_to_process=set(courses_to_prereqs)-set(pre)

    order=[]
    while courses_to_process:
        course=courses_to_process.pop()
        order.append(course)

        for c in suc[course]:
            pre[c].discard(course)
            if not pre[c]:
                courses_to_process.add(c)

    return order if len(order)==len(courses_to_prereqs) else []

assert toposort({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']
