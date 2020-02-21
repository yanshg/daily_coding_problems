#!/usr/bin/python

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

# About Python serialization/deserialization,
#  https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183

import json,pickle

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

class CustomEncoder(json.JSONEncoder):
    def default(self,o):
        return { '__{}__'.format(o.__class__.__name__): o.__dict__ }

def decode_object(o):
    if '__Node__' in o:
        node=Node('',None,None)
        node.__dict__.update(o['__Node__'])
        return node

    return o

def serialize(node):
    return json.dumps(node,indent=4,cls=CustomEncoder)

def deserialize(string):
    return json.loads(string,object_hook=decode_object)

def serialize_with_pickle(node):
    return pickle.dumps(node)

def deserialize_with_pickle(string):
    return pickle.loads(string)

node=Node('root', Node('left', Node('left.left')), Node('right'))
print(node)

serialized_str=serialize(node)
print(serialized_str)

new_node=deserialize(serialized_str)
assert new_node.left.left.val=='left.left'

# serialize/deserialize with pickle

serialized_str=serialize_with_pickle(node)
print(serialized_str)

new_node=deserialize_with_pickle(serialized_str)
assert new_node.left.left.val=='left.left'
