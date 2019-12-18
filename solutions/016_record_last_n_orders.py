#!/usr/bin/python

"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

"""

# Implementing a circular buffer suffices the requirement. It takes O(1) to record and get last ith.

class OrderLog:
    def __init__(self,size):
        self.orders=[None] * size
        self.size=size
        self.current_index=0

    def __repr__(self):
        return str(self.orders)

    def record(self,order_id):
        self.orders[self.current_index]=order_id
        self.current_index+=1
        if self.current_index>=self.size:
            self.current_index=0

    def get_last(self,i):
        index=(self.current_index-i+self.size)%self.size
        return self.orders[index]

orders=OrderLog(10)
orders.record(100)
orders.record(101)
assert orders.get_last(2)==100
