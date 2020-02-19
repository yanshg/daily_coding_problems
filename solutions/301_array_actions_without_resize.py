#!/usr/bin/python

"""

This problem was asked by Triplebyte.

Implement a data structure which carries out the following operations without resizing the underlying array:

    add(value): Add a value to the set of values.
    check(value): Check whether a value is in the set.

The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set), but should always correctly identify a true element.

"""

# Idea:   Bloom Filter

import hashlib

class BloomFilter:
    def __init__(self, n):
        self.size=n
        self.array=[False] * n
        self.hash_algorithms=[ hashlib.md5,
                               hashlib.sha1,
                               hashlib.sha256,
                               hashlib.sha384,
                               hashlib.sha512 ]
        self.hashes=[ self._get_hash(f) for f in self.hash_algorithms ]

    def _get_hash(self, f):
        def hash_function(value):
            h=f(str(value).encode('utf-8')).hexdigest()
            return int(h,16) % self.size

        return hash_function

    def add(self,value):
        for h in self.hashes:
            v=h(value)
            self.array[v]=True

    def check(self,value):
        for h in self.hashes:
            v=h(value)
            if not self.array[v]:
                return False
        return True


bf=BloomFilter(100)
bf.add(20)
assert bf.check(20)
assert not bf.check(30)

