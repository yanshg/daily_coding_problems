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

import sys

class GameOfLife(object):

    def __init__(self, cells):
        self.displacements = tuple((xd, yd) for yd in [-1, 0, 1] for xd in [-1, 0, 1] if xd != 0 or yd != 0)
        self.cells = set(cells)

    def __str__(self):
        xmin, xmax, ymin, ymax = [min_max(xy) for xy in zip(*self.cells) for min_max in [min, max]]
        return ''.join(('*' if (x, y) in self.cells else '.') + ('\n' if x == xmax else '')
                       for y in range(ymin, ymax + 1) for x in range(xmin, xmax + 1))

    def alive_next_round(self, x, y):
        neighbour_count = sum(1 if (x + xd, y + yd) in self.cells else 0 for xd, yd in self.displacements)
        return neighbour_count == 3 or ((x, y) in self.cells and neighbour_count == 2)

    def simulate(self, steps=1):
        for _ in range(steps):
            active_cells = set((x + xd, y + yd) for x, y in self.cells for xd in [-1, 0, 1] for yd in [-1, 0, 1])
            self.cells = set((x, y) for x, y in active_cells if self.alive_next_round(x, y))

return GameOfLife(cells)

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return "C(x={};y={})".format(self.x, self.y)

    def get_adjacent_coordinates(self):
        adjacent_coordinates = list()
        adjacent_coordinates.append(Coordinate(self.x, self.y - 1))
        adjacent_coordinates.append(Coordinate(self.x, self.y + 1))
        adjacent_coordinates.append(Coordinate(self.x - 1, self.y))
        adjacent_coordinates.append(Coordinate(self.x - 1, self.y - 1))
        adjacent_coordinates.append(Coordinate(self.x - 1, self.y + 1))
        adjacent_coordinates.append(Coordinate(self.x + 1, self.y))
        adjacent_coordinates.append(Coordinate(self.x + 1, self.y - 1))
        adjacent_coordinates.append(Coordinate(self.x + 1, self.y + 1))
        return adjacent_coordinates


def get_live_coordinates(all_live_coordinates, coordinates_to_check):
    count = 0
    for coordinate in coordinates_to_check:
        if coordinate in all_live_coordinates:
            count += 1

    return count


def update_liveness_neighbourhood(liveness_neighbourhood, adjacent_coordinates):
    for coordinate in adjacent_coordinates:
        if coordinate not in liveness_neighbourhood:
            liveness_neighbourhood[coordinate] = 0
        liveness_neighbourhood[coordinate] += 1


def play_iteration(board):
    coordinate_set = set(board)
    dead_coordinates = set()
    liveness_neighbourhood = dict()

    for coordinate in board:
        adjacent_coordinates = coordinate.get_adjacent_coordinates()
        live_adjacent_coordinate_count = get_live_coordinates(
            coordinate_set, adjacent_coordinates)
        update_liveness_neighbourhood(
            liveness_neighbourhood, adjacent_coordinates)

        if live_adjacent_coordinate_count < 2 or live_adjacent_coordinate_count > 3:
            dead_coordinates.add(coordinate)

    for coordinate in liveness_neighbourhood:
        if liveness_neighbourhood[coordinate] == 3:
            coordinate_set.add(coordinate)

    new_coordinate_set = coordinate_set - dead_coordinates

    return list(new_coordinate_set)


def print_board(coordinates):
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize

    if not coordinates:
        print(".")
        return

    for coordinate in coordinates:
        if coordinate.x < min_x:
            min_x = coordinate.x
        if coordinate.x > max_x:
            max_x = coordinate.x
        if coordinate.y < min_y:
            min_y = coordinate.y
        if coordinate.y > max_y:
            max_y = coordinate.y

    board = []
    for _ in range(max_x - min_x + 1):
        board.append(["."] * (max_y - min_y + 1))

    for coordinate in coordinates:
        board[coordinate.x - min_x][coordinate.y - min_y] = "*"

    for row in board:
        print(" ".join(row))


def play_game(initial_board, steps):
    print("\nPlaying Game of Life with the intial board:")
    print_board(initial_board)
    current_board = initial_board
    for step in range(steps):
        current_board = play_iteration(current_board)
        print("Iteration: {}".format(step))
        print_board(current_board)


# board is a list of Coordinates
board_0 = [
    Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 5)]
play_game(board_0, 3)


board_1 = [
    Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 5),
    Coordinate(2, 5), Coordinate(2, 6)]
play_game(board_1, 4)


board_2 = [
    Coordinate(0, 0), Coordinate(1, 0), Coordinate(1, 1),
    Coordinate(2, 5), Coordinate(2, 6), Coordinate(3, 9),
    Coordinate(4, 8), Coordinate(5, 10)]
play_game(board_2, 4)
