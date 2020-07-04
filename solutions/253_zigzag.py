#!/usr/bin/python

"""

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

"""

def get_spaces(k,row,desc):
    max_spaces = 2*(k-1)-1
    if desc:
        return max_spaces-2*row
    return max_spaces-2*(k-row-1)

def zigzag(s,k):
    n = len(s)
    for r in range(k):
        line = [' ']*n
        desc=True

        i = r
        while i < n:
            line[i] = s[i]
            i += get_spaces(k,r,desc) + 1
            desc = not desc

        print(''.join(line))

zigzag("thisisazigzag", 4)


