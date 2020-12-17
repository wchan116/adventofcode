from utils import get_input

from collections import defaultdict
from copy import deepcopy
from itertools import product


def get_occupied(grid, pos, directions, dim):
    occupied = 0
    for direction in directions:
        new_pos = (
            pos[0] + direction[0],
            pos[1] + direction[1],
            pos[2] + direction[2],
        )
        if dim == 4:
            new_pos += (pos[3] + direction[3],)
        if grid[new_pos] == "#":
            occupied += 1
    return occupied


def count_occupied(grid):
    return sum(1 for val in grid.values() if val == "#")


def get_positions(grid, directions, dim):
    positions = set()
    for pos in grid:
        for direction in directions:
            # new_pos = tuple(p + d for p, d in zip(pos, direction))
            new_pos = (
                pos[0] + direction[0],
                pos[1] + direction[1],
                pos[2] + direction[2],
            )
            if dim == 4:
                new_pos += (pos[3] + direction[3],)
            positions.add(new_pos)
    return positions


def get_directions(dim):
    return [x for x in product((-1, 0, 1), repeat=dim) if not all([c == 0 for c in x])]


def simulate(dim, ncycles=6):
    grid = defaultdict(lambda: ".")

    directions = get_directions(dim)

    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if dim == 3:
                grid[(i, j, 0)] = inp[j][i]
            elif dim == 4:
                grid[(i, j, 0, 0)] = inp[j][i]

    for i in range(ncycles):
        positions = get_positions(grid, directions, dim)
        new_grid = deepcopy(grid)
        for pos in positions:
            noccupied = get_occupied(grid, pos, directions, dim)
            if grid[pos] == "#" and not 2 <= noccupied <= 3:
                new_grid[pos] = "."
            elif grid[pos] == "." and noccupied == 3:
                new_grid[pos] = "#"
        grid = deepcopy(new_grid)
    return count_occupied(grid)


def p1(inp):
    return simulate(3)


def p2(inp):
    return simulate(4)


inp = get_input()
print(p1(inp))
print(p2(inp))
