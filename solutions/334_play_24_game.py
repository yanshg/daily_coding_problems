#!/usr/bin/python

"""

This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.

"""

# Backtracking

def operate(num1,num2,op):
    if op=='+': return num1+num2
    if op=='-': return num1-num2
    if op=='*': return num1*num2
    if op=='/': return num1/num2 if num2 else None

def play_24(nums):
    #print("nums:",nums)
    n=len(nums)
    if n==1:
        return nums[0]==24

    for i in range(n):
        for j in range(n):
            if i==j:
                continue

            consolidated_nums=[ num for k,num in enumerate(nums) if i!=k!=j ]
            for operator in "+-*/":
                new_num=operate(nums[i],nums[j],operator)
                if new_num is None:
                    continue
                if play_24(consolidated_nums+[new_num]):
                    return True
    return False

assert play_24([5, 2, 7, 8])
assert not play_24([1, 2, 1, 2])
