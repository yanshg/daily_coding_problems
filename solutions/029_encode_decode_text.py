#!/usr/bin/python

"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

"""

def encode(text):
    if not text:
        return ''

    first_ch,num=text[0],1
    for ch in text[1:]:
        if ch!=first_ch:
            break
        num+=1
    return str(num)+first_ch + encode(text[num:])

def decode(text):
    if not text:
        return ''

    num=0
    num_str,char='',''
    for ch in text:
        num+=1
        if not ch.isdigit():
            char=ch
            break
        num_str+=ch

    if not num_str.isdigit():
        raise ValueError("not correct format")

    return int(num_str) * ch + decode(text[num:])

assert encode("AAAABBBCCDAA")=="4A3B2C1D2A"
assert decode("4A3B2C1D2A")=="AAAABBBCCDAA"
