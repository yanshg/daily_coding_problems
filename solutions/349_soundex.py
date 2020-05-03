#!/usr/bin/python

"""

This problem was asked by Grammarly.

Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like M460.

One version of the algorithm is as follows:

    Remove consecutive consonants with the same sound (for example, change ck -> c).
    Keep the first letter. The remaining steps only apply to the rest of the string.
    Remove all vowels, including y, w, and h.
    Replace all consonants with the following digits:
        b, f, p, v -> 1
        c, g, j, k, q, s, x, z -> 2
        d, t -> 3
        l -> 4
        m, n -> 5
        r -> 6
    If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.

Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.

"""

# Idea:
#
#       name=~s/ck/c/g
#       name=~s/[aoeuiywh]//g
#       first=name[0]
#       name=name[1:]
#       name=~s/[bfpv]/1/g
#       name=~s/[cgjkqsxz]/2/g
#       name=~s/[dt]/3/g
#       name=~s/l/4/g
#       name=~s/[mn]/5/g
#       name=~s/r/6/g
#       return first+name

import re

def soundex(name):
    name=re.sub(r'ck','c',name)
    name=re.sub(r'cs','c',name)
    first=name[0]
    name=name[1:]
    name=re.sub(r'[aoeuiywh]','',name)
    name=re.sub(r'[bfpv]','1',name)
    name=re.sub(r'[cgjkqsxz]','2',name)
    name=re.sub(r'[dt]','3',name)
    name=re.sub(r'l','4',name)
    name=re.sub(r'[mn]','5',name)
    name=re.sub(r'r','6',name)

    name=(first+name)[:4]
    return "{:0<4}".format(name)

assert soundex('Jackson') == 'J250'
assert soundex('Jaxen') == 'J250'

