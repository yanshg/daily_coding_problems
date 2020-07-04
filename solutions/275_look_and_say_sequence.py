#!/usr/bin/python

"""

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.

"""

def look_and_say(s):
    result = ''

    prev,count='',0
    for c in s:
        if c == prev:
            count += 1
        else:
            if count:
                result += str(count)+prev
            prev = c
            count = 1
    result += str(count)+prev
    return result

def get_nth(n):
    s='1'
    print(s)
    for i in range(1,n):
        s=look_and_say(s)
        print(s)

    return s

get_nth(20)
