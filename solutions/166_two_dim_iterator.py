#!/usr/bin/python

"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

"""

class TwoDimIterator():
    def __init__(self,array):
        self.array=array
        self.generator=self.get_generator()
        self.next_val=next(self.generator)

    def get_generator(self):
        for arr in self.array:
            for num in arr:
                yield num

    def has_next(self):
        return self.next_val != None

    def next(self):
        val=self.next_val
        try:
            self.next_val=next(self.generator)
        except StopIteration:
            self.next_val=None

        return val


tdi=TwoDimIterator([[1, 2], [3], [], [4, 5, 6]])
assert tdi.has_next()
assert tdi.next()==1
assert tdi.next()==2
assert tdi.next()==3
assert tdi.next()==4
assert tdi.next()==5
assert tdi.next()==6
assert not tdi.has_next()
assert not tdi.next()
