#!/usr/bin/python

"""

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.

"""

# Idea:  https://en.wikipedia.org/wiki/Josephus_problem
#        https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212
#        https://www.geeksforgeeks.org/josephus-problem-set-2-simple-solution-k-2/

def last_exec(n, k):
    last_exec = None
    next_index = 0

    prisoners = list(range(1, n + 1))

    while prisoners:
        next_index = (next_index + k - 1) % len(prisoners)
        last_exec = prisoners[next_index]
        prisoners = prisoners[:next_index] + \
            prisoners[next_index + 1:]

    return last_exec

# Mathematics
# O(N)
def josephus(n, k):
    if (n == 1):
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1

# O(logN) for special case k=2
def josephus_2(n):
    p = 1
    while p <= n:
        p *= 2

    # Return 2n - 2^(1 + floor(Logn)) + 1
    return (2 * n) - p + 1

assert josephus(14,2)==13
assert josephus_2(14)==13
