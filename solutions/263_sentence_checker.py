#!/usr/bin/python

"""

This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

    The sentence must start with a capital letter, followed by a lowercase letter or a space.
    All other characters must be lowercase letters, separators (,;:) or terminal marks (.?!).
    There must be a single space between each word.
    The sentence must end with a terminal mark immediately following a word.

"""

import re

def is_valid_sentence(s):
    if not re.search(r'^[A-Z][a-z ]',s) or \
        not re.search(r'[a-z][\.\?!]$',s) or \
        re.search(r'  ',s):
        return False

    s=re.sub(r'[a-z,;:\.\?! ]','',s)
    if s!=s[0]:
        return False

    return True

assert is_valid_sentence("I love cinema.")
assert not is_valid_sentence("The vertex is S.")
assert is_valid_sentence("What are you doing?")
assert is_valid_sentence("I am single.")
assert not is_valid_sentence("I love Geeksquiz and Geeksforgeeks.")
assert not is_valid_sentence("My name is KG.")
assert not is_valid_sentence("I lovE cinema.")
assert not is_valid_sentence("GeeksQuiz. is a quiz site.")
assert not is_valid_sentence("  You are my friend.")
assert not is_valid_sentence("I love cinema")

