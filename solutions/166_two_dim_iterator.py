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
        self.generator=self.create_generator(array)
        self.next_val=None
        self.next(raise_exception=False)

    def create_generator(self,array):
        for item in array:
            if not item:
                continue
            if isinstance(item, list):
                for subitem in item:
                    yield subitem
            else:
                yield item

    def has_next(self):
        return self.next_val != None

    def next(self,raise_exception=True):
        if raise_exception and self.next_val is None:
            raise StopIteration

        val=self.next_val
        try:
            self.next_val=next(self.generator)
        except StopIteration:
            self.next_val=None

        return val


tdi=TwoDimIterator([[1, 2], 3, [], [4, 5, 6]])
assert tdi.has_next()
assert tdi.next()==1
assert tdi.next()==2
assert tdi.next()==3
assert tdi.next()==4
assert tdi.next()==5
assert tdi.next()==6
assert not tdi.has_next()
assert not tdi.next()
