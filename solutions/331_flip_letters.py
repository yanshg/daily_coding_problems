#!/usr/bin/python

"""

This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

"""

# Idea: Prefix Sum
#
#       |x|x|x|x|y|y|x|y|x|y|y|y|y|y|y|x|x|x|x|y|y|y|y|
#                            ^
#                            |
#                  lefty     |    rightx
#
#    filp lefty 'y's to 'x', and flip rightx 'x's to 'y'
#

def flip_letters(s):
    n=len(s)

    lefty=[0]*n
    rightx=[0]*n

    for i in range(1,n):
        lefty[i]=lefty[i-1]+(s[i-1]=='y')
    for i in range(n-2,-1,-1):
        rightx[i]=rightx[i+1]+(s[i+1]=='x')

    flips=n
    for i in range(n):
        flips=min(flips, lefty[i]+rightx[i])
    return flips

assert flip_letters('xyxxxyxyy')==2
