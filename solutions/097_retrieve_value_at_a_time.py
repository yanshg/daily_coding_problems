#!/usr/bin/python

"""

This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

    The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

    Consider the following examples:

        d.set(1, 1, 0) # set key 1 to value 1 at time 0
        d.set(1, 2, 2) # set key 1 to value 2 at time 2
        d.get(1, 1) # get key 1 at time 1 should be 1
        d.get(1, 3) # get key 1 at time 3 should be 2

        d.set(1, 1, 5) # set key 1 to value 1 at time 5
        d.get(1, 0) # get key 1 at time 0 should be null
        d.get(1, 10) # get key 1 at time 10 should be 1

        d.set(1, 1, 0) # set key 1 to value 1 at time 0
        d.set(1, 2, 0) # set key 1 to value 2 at time 0
        d.get(1, 0) # get key 1 at time 0 should be 2

"""

import bisect
from collections import defaultdict

class ValueTimeMap:
    def __init__(self):
        self.values=list()
        self.times=list()

    def __repr__(self):
        return str(list(zip(self.times,self.values)))

    def set(self,value,time):
        times,values=self.times,self.values
        index=bisect.bisect(times,time)
        if index<len(times) and times[index]==time:
            values[index]=value
        else:
            times.insert(index,time)
            values.insert(index,value)

    def get(self,time):
        times,values=self.times,self.values
        index=bisect.bisect(times,time)
        if not index:
            return None
        return values[index-1]

class KeyValueTimeMap:
    def __init__(self):
        self.keyvaluetime_map=defaultdict(ValueTimeMap)

    def __repr__(self):
        return str(self.keyvaluetime_map)

    def set(self,key,value,time):
        return self.keyvaluetime_map[key].set(value,time)

    def get(self,key,time):
        return self.keyvaluetime_map[key].get(time)


d=KeyValueTimeMap()
d.set(1, 1, 0)
d.set(1, 2, 2)
print(d)
assert d.get(1, 1)==1
assert d.get(1, 3)==2

d=KeyValueTimeMap()
d.set(1, 1, 5)
assert not d.get(1, 0)
assert d.get(1, 10)==1

d=KeyValueTimeMap()
d.set(1, 1, 0)
d.set(1, 2, 0)
assert d.get(1, 0)==2

