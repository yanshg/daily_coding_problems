#!/usr/bin/python

"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

# Idea:  Use recursion programming:
#        1. First add indepedent courses into order list
#        2. Then remove indepedent courses from prerequisite list.
#        3. Retry Step #1 and #2 untill prereqs become blank

def helper(prereqs,order):
    if not prereqs:
        return order

    indep=set()
    for course in prereqs:
        if not prereqs[course]:
            indep.add(course)
            order.append(course)

    for course in indep:
        del prereqs[course]

    for course in prereqs:
        prereqs[course]=set(prereqs[course])-indep

    return helper(prereqs,order)

def get_courses_order(prereqs):
    return helper(prereqs,[])

assert get_courses_order({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']
