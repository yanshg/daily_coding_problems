#!/usr/bin/python

"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

"""

import sys
import math

class BitArray:
    def __init__(self,size):
        self.size=size
        self.sizeofint=sys.getsizeof(0)
        self.bits=[0] * int(math.ceil(float(size)/self.sizeofint))

    def __repr__(self):
        return 'size:' + str(self.size) + ',sizeof(0):' + str(self.sizeofint) + ',' + str(self.bits)

    def check_bound(self,i):
        if i>=self.size:
            raise IndexError('Out of bound')

    def set(self,i,val):
        self.check_bound(i)
        index=i//self.sizeofint
        offset=i%self.sizeofint
        mask=1<<(self.sizeofint-offset)
        if val:
            self.bits[index]|=mask
        else:
            self.bits[index]&=~mask


    def get(self,i):
        self.check_bound(i)
        index=i//self.sizeofint
        offset=i%self.sizeofint
        mask=1<<(self.sizeofint-offset)
        if self.bits[index] & mask:
            return 1
        return 0

ba=BitArray(100)
print(ba)
ba.set(10,1)
ba.set(60,1)
print(ba)

assert ba.get(10)==1
assert ba.get(60)==1
assert ba.get(11)==0
