#!/usr/bin/python

"""

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.

"""

# Use DP table

# DP[n][k] means minimum number ot trials with n eggs and k floors
#
# Base case:  DP[1][k]=k
#             DP[n][0]=0
#             DP[n][1]=1
#
# Tranforming:
#             DP[n][k] = min([1+(max(DP[n][k-x], DP[n-1][x-1) for x in range(k)])

INT_MAX = 32767

# Function to get minimum number of trials needed in worst case with n eggs and k floors
def egg_drop(n, k):
    egg_floor = [[0 for x in range(k + 1)] for x in range(n + 1)]

    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, n + 1):
        egg_floor[i][1] = 1
        egg_floor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        egg_floor[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            egg_floor[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(egg_floor[i-1][x-1], egg_floor[i][j-x])
                if res < egg_floor[i][j]:
                    egg_floor[i][j] = res

    return egg_floor[n][k]

n = 2
k = 36
print("Minimum number of trials in worst case with " + str(n) + " eggs and "
       + str(k) + " floors is " + str(egg_drop(n, k)))
