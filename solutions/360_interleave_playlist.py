#!/usr/bin/python

"""

This problem was asked by Spotify.

You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. For example, the list [4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}. In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].

"""

# Topological sort

from collections import defaultdict

def build_graph(lists):
    pre=defaultdict(set)
    suc=defaultdict(set)
    for songs in lists:
        for i in range(len(songs)-1):
           s1,s2=songs[i],songs[i+1]
           if s1 in suc[s2] or s2 in pre[s1]:
               raise ValueError("{} and {} are out of order in input".format(s1,s2))

           pre[s2].add(s1)
           suc[s1].add(s2)

    print("pre:",pre,"\nsuc:",suc)
    return pre,suc

def get_playlist(lists):
    try:
        pre,suc=build_graph(lists)
    except Exception as e:
        print(e)
        return None

    order=[]

    songs=set([s for s in pre if not pre[s]])
    while songs:
        s=songs.pop()
        order+=[s]
        for s1 in suc[s]:
            pre[s1].discard(s)
            if not pre[s1]:
                songs.add(s1)

    return order

assert get_playlist(([1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]))==[2,1,6,7,3,9,5]
