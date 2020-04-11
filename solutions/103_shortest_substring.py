#!/usr/bin/python

"""

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

"""

# Idea: Record the last position of the character, and trim the substring from the start
#
#       One test case with multiple candidate substrings, like: "figehaeciea" with set {a, e i}
#                                                 3 candidates: "igeha", "aeci", "iea"

def get_shortest_substring(string,chars):
    positions=dict()
    candidate=None

    start=0
    for i,c in enumerate(string):
        if c not in chars:
            continue

        # Record the last position of the character
        positions[c]=i

        # Trim the substring
        while start<i and (string[start] not in chars or start<positions[string[start]]):
            start+=1

        # get the candidate substring
        if len(positions)==len(chars):
            if not candidate or i-start+1<len(candidate):
                candidate=string[start:i+1]
                print("candidate: ",candidate)

    print("Final smallest substring: ",candidate)
    return candidate

assert get_shortest_substring("figehaeci","aei")== "aeci"
assert get_shortest_substring("figehaeciea","aei")== "iea"
assert not get_shortest_substring("abcdedbc", "gf")
assert get_shortest_substring("abccbbbccbcb", "abc") == "abc"
assert get_shortest_substring("abcdedbc", "db") == "db"
assert get_shortest_substring("abcdedbc", "bc") == "bc"
assert get_shortest_substring("abcdecdb", "bc") == "bc"
assert get_shortest_substring("abcdecdb", "bce") == "bcde"

