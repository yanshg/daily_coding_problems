#!/usr/bin/python

"""

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

"""

# Idea:  use list(zip(*cells)) to get ((list of x), (list of y)) from cells

class ConwayGameLife():
    def __init__(self,cells):
        self.cells=set(cells)

    def __repr__(self):
        xs,ys=list(zip(*self.cells))
        xmin,xmax,ymin,ymax=min(xs),max(xs),min(ys),max(ys)
        return ''.join(('*' if (x,y) in self.cells else '.') + ('\n' if x==xmax else '') \
                       for y in range(ymin,ymax+1) for x in range(xmin,xmax+1))

    def show_cells(self):
        print("==============")
        print(str(self))

    def active_next_round(self,x,y):
        neighbours=[(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        neighbour_count=sum(1 if (x,y) in self.cells else 0 for (x,y) in neighbours)
        return neighbour_count==3 or (neighbour_count==2 and (x,y) in self.cells)

    def process_to_next_round(self):
        active_cells=set((x+xd,y+yd) for (x,y) in self.cells for xd in [-1,0,1] for yd in [-1,0,1])
        self.cells=set((x,y) for (x,y) in active_cells if self.active_next_round(x,y))

    def play(self,steps):
        self.show_cells()
        for step in range(steps):
            self.process_to_next_round()
            self.show_cells()

game1=ConwayGameLife([(0,0),(1,0),(1,1),(2,5),(2,6),(3,9),(4,8),(5,9),(5,10)])
game1.play(4)
