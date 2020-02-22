#!/usr/bin/python

"""

This problem was asked by Twitter.

You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:

    update(hour: int, value: int): Increment the element at index hour by value.
    query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).

You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.

"""

# O(log n)

class BIT:
    def __init__(self,nums):
        self.size=len(nums)
        self.tree=[0]*(self.size+1)
        for i,num in enumerate(nums):
            self.update(i+1,num)

    def _check_bound(self,index):
        if index<0 or index>self.size:
            raise(IndexError, "Index out of bounds")

    def update(self,index,value):
        self._check_bound(index)
        while index<=self.size:
            self.tree[index]+=value
            index+=index&-index

    def query(self,index):
        self._check_bound(index)
        total=0
        while index>0:
            total+=self.tree[index]
            index-=index&-index
        return total

class Subscribers:
    def __init__(self,nums):
        self.subscribers=nums
        self.bit=BIT(nums)

    def update(self,i,num):
        prev=self.subscribers[i]
        self.subscribers[i]=num
        self.bit.update(i+1,num-prev)

    def query(self,start,end):
        return self.bit.query(end+1) - self.bit.query(start)


sub=Subscribers([3,5,8,3,5, 2,5,9,6,12, 6,4,7,2,5, 7,6,9,2,4, 4,6,7,8])
assert sub.query(0,4)==24
assert sub.query(5,9)==34

sub.update(6,11)
assert sub.query(5,9)==40
