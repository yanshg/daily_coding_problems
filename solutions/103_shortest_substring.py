#!/usr/bin/python

"""

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

"""

# Idea:
#    1. Get all occurance position of the characters in the string
#    2. Use the position information to improve search performance
#    3. Discard the previous found poistion if symetrix,
#       for example for set "aief", found a..i..e..i..a in the original string, then discard the first found "a..i..".

def get_shortest_substring(string,chars):
    candidate=None

    pos_queue,char_queue,seen=list(),list(),set()

    for i,ch in enumerate(string):
        if ch not in chars:
            continue

        pos_queue.append(i)
        char_queue.append(ch)
        seen.add(ch)

        shift=0
        for k in range(len(char_queue)//2):
            if char_queue[k]==char_queue[-k-1]:
                shift+=1
            else:
                break

        if shift!=0:
            pos_queue=pos_queue[shift:]
            char_queue=char_queue[shift:]

        if len(seen)==len(chars):
            if not candidate or len(candidate)>pos_queue[-1]-pos_queue[0]+1:
                candidate=string[pos_queue[0]:(pos_queue[-1]+1)]

    return candidate


assert get_shortest_substring("figehaeci","aei")== "aeci"
assert not get_shortest_substring("abcdedbc", "gf")
assert get_shortest_substring("abccbbbccbcb", "abc") == "abc"
assert get_shortest_substring("abcdedbc", "db") == "db"
assert get_shortest_substring("abcdedbc", "bc") == "bc"
assert get_shortest_substring("abcdecdb", "bc") == "bc"
assert get_shortest_substring("abcdecdb", "bce") == "bcde"

