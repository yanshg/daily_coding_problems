#!/usr/bin/python

"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

return 6.

"""

#   (tlx1, tly1)               (tlx2, tly2)
#              |-------|                  |--------|
#              |       |                  |        |
#              |-------|                  |--------|
#                     (brx1, bry1)                 (brx2, bry2)


class Rectangle:
    def __init__(self,top_left,dimensions):
        self.top_left=top_left
        self.dimensions=dimensions
        self.bottom_right=(top_left[0]+dimensions[0], top_left[1]-dimensions[1])

    def __repr__(self):
        return "{}-{}".format(self.top_left,self.bottom_right)


def get_intersection_area(rect1,rect2):
    print("rectangle 1: ", rect1)
    print("rectangle 2: ", rect2)
    tlx1,tly1=rect1.top_left
    brx1,bry1=rect1.bottom_right
    tlx2,tly2=rect2.top_left
    brx2,bry2=rect2.bottom_right

    # No intersections cases:
    # 1. Rectange2 on top of Rectangle1
    # 2. Rectange2 under Rectangle1
    # 3. Rectange2 on left of Rectangle1
    # 4. Rectange2 on right of Rectangle1
    if bry2>=tly1 or tly2<=bry1 or brx2<=tlx1 or tlx2>=brx1:
        return 0

    # top left point of the overlapping area.
    tlx_o=max(tlx1,tlx2)
    tly_o=min(tly1,tly2)

    # bottom right point of the overlapping area.
    brx_o=min(brx1,brx2)
    bry_o=max(bry1,bry2)

    return (tly_o - bry_o) * (brx_o - tlx_o)

assert get_intersection_area(Rectangle((1,4),(3,3)), Rectangle((0,5),(4,3)))==6
