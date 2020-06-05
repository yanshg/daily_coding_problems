#!/usr/bin/python

"""

This problem was asked by Google.

Implement a key value store, where keys and values are integers, with the following methods:

    update(key, vl): updates the value at key to val, or sets it if doesn't exist
    get(key): returns the value with key, or None if no such value exists
    max_key(val): returns the largest key with value val, or None if no key with that value exists

For example, if we ran the following calls:

kv.update(1, 1)
kv.update(2, 1)

And then called kv.max_key(1), it should return 2, since it's the largest key with value 1.

"""

class KVStore():
    def __init__(self):
        self._dict=dict()
        self._max_key=dict()

    def update(self,key,val):
        self._dict[key]=val
        old_max_key=self._max_key.get(val,float('-inf'))
        self._max_key[val]=max(key,old_max_key)

    def get(self,key):
        self._dict.get(key)

    def max_key(self,val):
        return self._max_key.get(val)

kvs=KVStore()
kvs.update(1,1)
kvs.update(2,1)
assert kvs.max_key(1)==2
assert kvs.max_key(2)==None
