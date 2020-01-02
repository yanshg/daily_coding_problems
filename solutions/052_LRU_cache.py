#!/usr/bin/python

"""

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

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

class Node:
    def __init__(self,key,value,next=None,prev=None):
        self.key=key
        self.value=value
        self.next=next
        self.prev=prev

    def __repr__(self):
        return "({}=>{})<->{}".format(self.key,self.value,self.next)

# Double end queue specific for cache
class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __repr__(self):
        return str(self.head)

    def __len__(self):
        return self.size

    def append(self,node):
        if not self.head:
            self.head=node
            node.prev=None

        if self.tail:
            self.tail.next=node
            node.prev=self.tail
        self.tail=node

        node.next=None
        self.size+=1

    def popleft(self):
        return self.remove(self.head)

    def remove(self,node):
        if not node:
            return None

        prev_node=node.prev
        next_node=node.next
        if prev_node:
            prev_node.next=next_node
        else:
            # removing the head node
            self.head=next_node

        if next_node:
            next_node.prev=prev_node
        else:
            # removing the tail node
            self.tail=prev_node

        self.size-=1

        # clean the node
        node.prev=None
        node.next=None

        return node

class LRUcache:
    def __init__(self,n):
        self.size=n
        self.deque=Deque()
        self.hashmap=dict()

    def __repr__(self):
        return str(self.deque)

    def set(self,key,value):
        # sets key to value.
        # If there are already n items in the cache and we are adding a new item,
        # then it should also remove the least recently used item.
        if not key:
            return

        if key in self.hashmap:
            node=self.hashmap[key]
            if node:
                self.deque.remove(node)
                self.deque.append(node)
                node.value=value
        else:
            node=Node(key,value)
            self.hashmap[key]=node
            self.deque.append(node)
            if len(self.deque)>self.size:
                node_to_remove=self.deque.popleft()
                if node_to_remove:
                    del self.hashmap[node_to_remove.key]

    def get(self,key):
        # gets the value at key. If no such key exists, return null.
        if key and key in self.hashmap:
            node=self.hashmap[key]
            if node:
                self.deque.remove(node)
                self.deque.append(node)
                return node.value

        return None

cache=LRUcache(3)
cache.set('hello', 20)
cache.set('world', 30)
print("cache:", cache)

assert cache.get('hello') == 20
assert cache.get('world') == 30

cache.set('haha', 'fine')
cache.set('emmm', 'not good')

print("cache:", cache)

assert not cache.get('hello')
assert cache.get('haha') == 'fine'
assert cache.get('emmm') == 'not good'

