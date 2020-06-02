#!/usr/bin/python

"""

This problem was asked by Salesforce.

The number 6174 is yyknown as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

    For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
    Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

    4321 - 1234 = 3087
    8730 - 0378 = 8352
    8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.

"""

# Method with no DP.
def kaprekar_process_normal(num):
    steps=0
    prev=num

    while True:
        digits=sorted(str(num))
        if len(set(digits))<=2:
            break

        smaller=int(''.join(digits))
        larger=int(''.join(reversed(digits)))

        num=larger-smaller
        steps+=1

        if num==prev:
            #print("constant:",num)
            return steps-1

        prev=num

    return 0

# DP method
def helper(num,prev,steps):
    if num==prev:
        #print("constant:",num)
        return steps-1

    digits=sorted(str(num))
    smaller=int(''.join(digits))
    larger=int(''.join(reversed(digits)))

    return helper(larger-smaller,num,steps+1)

def kaprekar_process(num):
    if len(set(str(num)))<=2:
        return 0

    return helper(num,0,0)

assert kaprekar_process_normal(8889)==0
assert kaprekar_process(8889)==0
assert kaprekar_process(4321)==3

for num in range(1000,10000):
    steps=kaprekar_process(num)
    print("num:", num, "steps:",steps)
