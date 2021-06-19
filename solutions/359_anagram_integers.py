#!/usr/bin/python

"""

This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.

"""

# Idea: Backtracking

from collections import Counter

digit_words=[ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

def extract_counts(counts,word):
    results=counts.copy()
    for c in word:
        if c not in counts:
            return None

        results[c]-=1
        if results[c]==0:
            del results[c]

    return results

def backtrack(counts,mapped_digits,digits):
    if not counts:
        return mapped_digits

    for digit in digits:
        remaining=extract_counts(counts, digit_words[digit])
        if remaining is not None:
            result=backtrack(remaining, mapped_digits+str(digit), digits-set(range(digit)))
            if result:
                return result

    return ''

def get_integers(s):
    counts=Counter(s)
    result=backtrack(counts, '', set(range(10)))
    if result:
        return int(result)
    return -1

assert get_integers('niesevehrtfeev') == 357
assert get_integers('niesevehrtfees') == -1
