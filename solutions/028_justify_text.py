#!/usr/bin/python

"""

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
 "fox  jumps  over", # 2 extra spaces distributed evenly
 "the   lazy   dog"] # 4 extra spaces distributed evenly

"""

def justify_text(words,line_width):
    if not words:
        return []

    num,width=0,0
    for word in words:
        if width + num + len(word) > line_width:
            break
        width+=len(word)
        num+=1

    gaps=num-1
    gap_len=line_width-width
    first_gap_add=0
    if gaps>0:
        first_gap_add=gap_len % gaps
        gap_len=gap_len // gaps

    first_line=words[0]+' '*(gap_len+first_gap_add) + (' '*gap_len).join(words[1:num])

    return [ first_line ] + justify_text(words[num:],line_width)

assert justify_text(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)== ["the  quick brown","fox  jumps  over","the   lazy   dog"]
