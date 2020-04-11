#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.

"""

# Idea:  Record each character's last position, and trim the substring from the start position
#
#        Need have one test case with muliple candidate substrings, like: "jiiujiiiitsujiiiktuiisjuiiiij",
#                                                           2 candidates: "tsujiiik", "ktuiisj"

def get_smallest_window(string):
    chars=set(string)
    candidate=''

    positions=dict()
    start=0
    for i,c in enumerate(string):
        # Record the last position of the character
        positions[c]=i

        # Trim the substring
        while start<i and start<positions[string[start]]:
            start+=1

        # Get candidate substring
        if len(positions)==len(chars):
            if not candidate or i-start+1<len(candidate):
                candidate=string[start:i+1]
                print("candidate: ", candidate)

    print("Final smallest substring: ", candidate)
    return len(candidate)

assert get_smallest_window("jiujitsu")==5
assert get_smallest_window("jiiujiiiitsujiiiktuiisjuiiiij")==7
