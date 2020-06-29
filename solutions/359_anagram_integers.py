#!/usr/bin/python

"""

This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.

"""

# Idea: Backtracking

from collections import Counter

digit_word_map={
   '0': 'zero',
   '1': 'one',
   '2': 'two',
   '3': 'three',
   '4': 'four',
   '5': 'five',
   '6': 'six',
   '7': 'seven',
   '8': 'eight',
   '9': 'nine',
}

def extract_counts(counts,word):
    for c in word:
        if c not in counts:
            return None

        counts[c]-=1
        if counts[c]==0:
            del counts[c]

    return counts

def backtrack(counts,mapped_digits,digits):
    print("counts:", counts, "mapped_digits:", mapped_digits)
    if not counts:
        return mapped_digits

    for digit in digits:
        remaining=extract_counts(counts, digit_word_map[digit])
        if remaining is not None:
            result=backtrack(remaining, mapped_digits+digit, digits)
            if result:
                return result

    return ''

def get_integers(s):
    counts=Counter(s)
    result=backtrack(counts, '', set(digit_word_map))
    if result:
        return int(''.join(sorted(list(result))))
    return -1

assert get_integers('niesevehrtfeev') == 357
assert get_integers('niesevehrtfees') == -1
