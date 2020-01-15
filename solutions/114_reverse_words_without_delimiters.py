#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

"""

# Notes:
#    string.replace("str",word): the original 'string' do not change
#    string.format(*words):      Need use "*list" to convert a list or tuple to real list.
#    words.reverse():            In place reverse the items in the list
#    reversed(words):            return reversed list, the original list do not change


def reverse_words(string,delimiters):
    replace_string=""
    words=[]

    word=""
    for char in string:
        if char in delimiters:
            if word:
                words.append(word)
                replace_string+="{}"
                word=""
            replace_string+=char
        else:
            word+=char

    if word:
        words.append(word)
        replace_string+="{}"

    words.reverse()

    return replace_string.format(*words) 

assert reverse_words("hello/world:here","/:") == "here/world:hello"
assert reverse_words("hello/world:here/","/:") == "here/world:hello/"
assert reverse_words("hello//world:here","/:") == "here//world:hello"
