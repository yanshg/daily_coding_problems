#!/usr/bin/python

"""

This problem was asked by Spotify.

Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15

"""

# Article:  https://www.geeksforgeeks.org/dice-throw-dp-30/

# f(N,faces,total) = f(N-1,faces,total-1) + f(N-1,faces,total-2) + ... + f(N-1,faces,total-min(faces,total-N+1))
#                    | first dice is 1  |   | first dice is 2  |         | first dice is faces or total-N+1    |


def throw_dice(n, faces, total):
    max_num = n*faces
    if total >= max_num:
        return int(total==max_num)

    min_num = n
    if total <= min_num:
        return int(total==min_num)

    cache=[ [0]*(total+1) for i in range(n+1) ]
    for j in range(1,min(faces+1,total+1)):
        cache[1][j]=1

    for i in range(2,n+1):
        for j in range(i,total+1):
            for k in range(1,min(faces+1,j)):
                 cache[i][j]+=cache[i-1][j-k]

    return cache[-1][-1]

assert throw_dice(1,6,3) == 1
assert throw_dice(1,6,6) == 1
assert throw_dice(1,6,7) == 0
assert throw_dice(3,6,2) == 0
assert throw_dice(3,6,3) == 1
assert throw_dice(3,6,5) == 6
assert throw_dice(3,6,7) == 15
assert throw_dice(3,6,18) == 1
assert throw_dice(3,6,19) == 0
