#!/usr/bin/python

"""

This problem was asked by Dropbox.

Create a data structure that performs all the following operations in O(1) time:

    plus: Add a key with value 1. If the key already exists, increment its value by one.
    minus: Decrement the value of a key. If the key's value is currently 1, remove it.
    get_max: Return a key with the highest value.
    get_min: Return a key with the lowest value.

"""

class MaxMinDict():
    def __init__(self):
        self._dict=dict()
        self._max_keys=set()
        self._min_keys=set()

    def plus(self,key):
        max_value=self._get_max_value()
        min_value=self._get_min_value()

        if key in self._dict:
            self._dict[key]+=1
        else:
            self._dict[key]=1

        value=self._dict[key]
        if not self._max_keys or \
           key in self._max_keys or \
           value>max_value:
            self._max_keys={key}
        elif value==max_value:
            # current key is not in self._max_keys
            self._max_keys.add(key)

        if not self._min_keys or \
           value<min_value:
            self._min_keys={key}
        elif key in self._min_keys:
            self._min_keys.discard(key)

    def minus(self,key):
        if key not in self._dict:
            return

        max_value=self._get_max_value()
        min_value=self._get_min_value()

        self._dict[key]-=1
        if self._dict[key]<=0:
            del self._dict[key]

    def get_max(self):
        return self._max_keys[0] if self._max_keys else None

    def get_min(self):
        return self._min_keys[0] if self._min_keys else None

    def _get_max_value(self):
        max_key=self.get_max()
        return self._dict[max_key] if max_key and max_key in self._dict else 0

    def _get_min_value(self):
        min_key=self.get_min()
        return self._dict[min_key] if min_key and min_key in self._dict else 0

mm=MaxMinDict()
assert mm.get_max()==None
assert mm.get_min()==None

mm.plus('k1')
assert mm.get_max()=='k1'
assert mm.get_min()=='k1'

mm.plus('k1')
mm.plus('k2')
assert mm.get_max()=='k1'
assert mm.get_min()=='k2'

mm.minus('k2')
assert mm.get_max()=='k1'
assert mm.get_min()=='k1'
