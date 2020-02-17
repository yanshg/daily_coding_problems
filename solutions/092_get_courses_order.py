#!/usr/bin/python

"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

# Idea:  Topological sort on a graph. use BFS with deque

#        Use recursion programming:
#        1. First add indepedent courses into order list
#        2. Then remove indepedent courses from prerequisite list.
#        3. Retry Step #1 and #2 untill prereqs become blank

from collections import deque,defaultdict

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


def get_courses_order_with_bfs(course_to_prereqs):
    course_to_prereqs={ c:set(p) for c,p in course_to_prereqs.items() }
    indep=deque([c for c,p in course_to_prereqs.items() if not p])

    prereq_to_courses=defaultdict(list)
    for course,prereqs in course_to_prereqs.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].append(course)

    result=[]
    while indep:
        prereq=indep.popleft()
        result.append(prereq)

        for course in prereq_to_courses[prereq]:
            course_to_prereqs[course].remove(prereq)
            if not course_to_prereqs[course]:
                indep.append(course)

    if len(result) != len(course_to_prereqs):
        return None

    return result


assert get_courses_order({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']
assert get_courses_order_with_bfs({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']
