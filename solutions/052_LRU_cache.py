#!/usr/bin/python

"""

This problem was asked by Google.

Implement an LRUCache (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

"""

# Idea: Need implement a double end queue with doubly linked list to save the cached sequence information.
#       so that we can remove a node from middle of the queue with O(1).
#       we can not directly use collections.deque() since it is not O(1) to remove an element
#
# Double end queue:
#
#       |--------|         |--------|         |--------|
#       |  key1  |  ---->  |  key2  |  ---->  |  key3  |
#       | value1 |  <----  | value2 |  <----  | value3 |
#       |--------|         |--------|         |--------|
#
# Need implement: append(), popleft(), remove()
#
# For Hashmap:  key1 -> Node1
#               key2 -> Node2


CAPACITY = 128

class CacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = CacheNode('HEAD', None)
        self.tail = CacheNode('TAIL', None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        keys = list()
        node = self.head.next
        while node != self.tail:
            keys += [ str(node.key) ]
            node = node.next
        return ','.join(keys)

    def add(self, node):
        if node:
            node.prev = self.head
            node.next = self.head.next
            node.next.prev = node
            self.head.next = node

    def remove(self, node):
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev

    def get_tail(self):
        tail = self.tail.prev
        return tail if tail != self.head else None

class LRUCache:
    def __init__(self, capacity=CAPACITY):
        self.capacity = capacity
        self.hashmap = dict()
        self.linkedlist = DoubleLinkedList()

    def __repr__(self):
        return str(self.linkedlist)

    def get(self, key):
        if key not in self.hashmap:
            return None

        node = self.hashmap[key]
        linkedlist = self.linkedlist
        linkedlist.remove(node)
        linkedlist.add(node)
        return node.value

    def put(self, key, value):
        linkedlist = self.linkedlist

        if key in self.hashmap:
            node = self.hashmap[key]
            linkedlist.remove(node)
            linkedlist.add(node)
            node.value = value
            return

        node = CacheNode(key, value)
        linkedlist.add(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            tail = linkedlist.get_tail()
            if tail:
                linkedlist.remove(tail)
                del self.hashmap[tail.key]

cache = LRUCache(3)
cache.put(1, 'hello1')
cache.put(2, 'hello2')
cache.put(3, 'hello3')
cache.put(4, 'hello4')

assert not cache.get(1)
assert cache.get(4) == 'hello4'

