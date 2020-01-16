#!/usr/bin/python

"""
This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

"""

OPERANDS={'+','-','*','/'}

def evaluate_arithmetic(notation):
    stack=list()

    for exp in notation:
        if exp in OPERANDS:
            op2=stack.pop()
            op1=stack.pop()
            result=eval(str(op1)+exp+str(op2))
            stack.append(result)
        else:
            stack.append(exp)

    return stack[-1]

assert evaluate_arithmetic([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])==5

