#!/usr/bin/python

"""

This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s

With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.

"""

# Idea:  use heap to sort the characters and then generate the binary tree

import heapq

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def build_huffman_tree(char_freq_dict):
    hq=[]
    for c,freq in char_freq_dict.items():
        heapq.heappush(hq, (freq, Node(c)))
        
    while len(hq)>1:
        f1,n1=heapq.heappop(hq)
        f2,n2=heapq.heappop(hq)
        heapq.heappush(hq,(f1+f2,Node('*',n1,n2)))

    freq,root=heapq.heappop(hq)
    return root

def encode(root,string='',mapping={}):
    if not root:
        return mapping

    if not root.left and not root.right:
        mapping[root.val]=string
        return mapping

    encode(root.left,string+'0',mapping)
    encode(root.right,string+'1',mapping)

    return mapping

def get_huffman_mapping(char_freq_dict):
    root=build_huffman_tree(char_freq_dict)
    print("Freqency: ",char_freq_dict, "Tree: ",root)
    return encode(root,'',{})

assert get_huffman_mapping({'a':3, 'c':6, 'e':8, 'f':2})=={'e':'0', 'f':'100', 'a':'101', 'c':'11'}
