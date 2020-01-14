#!/usr/bin/python

"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.
"""

class SparseArray:
    def __init__(self,arr,size):
        self._dict=dict()
        self.size=size
        for i,val in enumerate(arr):
            self.set(i,val)

    def _check_bounds(self,i):
        if i<0 or i>=self.size:
            raise IndexError("Out Of Bound")

    def set(self,i,val):
        self._check_bounds(i)

        if val!=0:
            self._dict[i]=val
        elif i in self._dict:
            del self._dict[i]

    def get(self,i):
        self._check_bounds(i)
        return self._dict.get(i,0)

sa=SparseArray([1,1,2,3], 100)

sa.set(50, 32)
#sa.set(110, 32)
assert sa.get(0)==1
assert sa.get(20)==0
assert sa.get(50)==32
#assert sa.get(110)

