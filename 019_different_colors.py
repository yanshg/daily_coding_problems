#!/usr/bin/python

"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

"""

# Matrix:
#              color1   color2   color3
#    house1     h11      h12      h13
#    house2     h21      h22      h23
#    house3     h31      h32      h33
#    house4     h41      h42      h43
#    house5     h51      h52      h53
#    house6     h61      h62      h63
#    house7     h71      h72      h73
#    house8     h81      h82      h83
#    house9     h91      h92      h93

def get_minimum_painting_cost(matrix):
    # best_costs[i][j]:  record the minimum cost if use j color for the house i
    # best_costs[i][j] = min(best_costs[i-1] except j column) + matrix[i][j]
    # We only need record the last best_costs[] to calculate current best_costs[]
    colors=len(matrix[0])
    best_costs=[0] * colors
    for costs in matrix:
        new_costs=list()
        for i in range(colors):
            new_costs.append(costs[i]+min(best_costs[:i]+best_costs[i+1:]))
        best_costs=new_costs
    return min(best_costs)

cost_matrix = [[7,  3, 8, 6, 1, 2],
               [5,  6, 7, 2, 4, 3],
               [10, 1, 4, 9, 7, 6]]
assert get_minimum_painting_cost(cost_matrix) == 4

cost_matrix = [[7,  3, 8, 6, 1, 2],
               [5,  6, 7, 2, 4, 3],
               [10, 1, 4, 9, 7, 6],
               [10, 1, 4, 9, 7, 6]]
assert get_minimum_painting_cost(cost_matrix) == 8

