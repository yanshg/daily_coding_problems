#!/usr/bin/python

"""

This problem was asked by Google.

You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 4)
}

return true as the first and third rectangle overlap each other.

"""

class Rectangle:
    def __init__(self,json):
        self.top_left=json['top_left']
        self.dimensions=json['dimensions']
        self.bottom_right=(self.top_left[0]+self.dimensions[0], self.top_left[1]-self.dimensions[1])

    def overlap(self, other):
        tlx1,tly1=self.top_left
        brx1,bry1=self.bottom_right

        tlx2,tly2=other.top_left
        brx2,bry2=other.bottom_right

        if tlx1<=tlx2 and tly1>=tly2 and brx1>=brx2 and bry1<=bry2:
            return True

        return False

def contain_overlapping_pair(rects):
    n=len(rects)
    for i in range(n-1):
        for j in range(i+1,n):
            if rects[i].overlap(rects[j]) or \
                    rects[j].overlap(rects[i]):
                return True
    return False

# example provided in the question is incorrect
r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 4)})
assert contain_overlapping_pair([r1, r2, r3])

r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 3)})
assert not contain_overlapping_pair([r1, r2, r3])
