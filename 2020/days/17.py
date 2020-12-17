from utils import get_input

from collections import defaultdict
from copy import deepcopy


def get_occupied(grid, pos, directions):
    occupied = 0
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])
        if grid[new_pos] == "#":
            occupied += 1
    return occupied


def get_occupied4d(grid, pos, directions):
    occupied = 0
    for direction in directions:
        new_pos = (
            pos[0] + direction[0],
            pos[1] + direction[1],
            pos[2] + direction[2],
            pos[3] + direction[3],
        )
        if grid[new_pos] == "#":
            occupied += 1
    return occupied


def count_occupied(grid):
    noccupied = 0
    for val in grid.values():
        if val == "#":
            noccupied += 1
    return noccupied


def get_positions(grid, directions):
    positions = set()
    for pos in grid:
        for direction in directions:
            new_pos = (
                pos[0] + direction[0],
                pos[1] + direction[1],
                pos[2] + direction[2],
            )
            positions.add(new_pos)
    return positions


def get_positions4d(grid, directions):
    positions = set()
    for pos in grid:
        for direction in directions:
            new_pos = (
                pos[0] + direction[0],
                pos[1] + direction[1],
                pos[2] + direction[2],
                pos[3] + direction[3],
            )
            positions.add(new_pos)
    return positions


def get_directions():
    dirs = []
    ways = [-1, 0, 1]
    for x in ways:
        for y in ways:
            for z in ways:
                for w in ways:
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    dirs.append((x, y, z, w))
    return dirs


def p1(inp):
    # fmt: off
    directions = {
        (-1, -1, -1), (0, -1, -1), (1, -1, -1),
        (-1, 0, -1), (0, 0, -1), (1, 0, -1),
        (-1, 1, -1), (0, 1, -1), (1, 1, -1),

        (-1, -1, 0), (0, -1, 0), (1, -1, 0),
        (-1, 0, 0),            (1, 0, 0),
        (-1, 1, 0), (0, 1, 0), (1, 1, 0),

        (-1, -1, 1), (0, -1, 1), (1, -1, 1),
        (-1, 0, 1), (0, 0, 1), (1, 0, 1),
        (-1, 1, 1), (0, 1, 1), (1, 1, 1)
    }
    # fmt: on
    grid = defaultdict(lambda: ".")
    cycle = 6

    # initialise input
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            grid[(i, j, 0)] = inp[j][i]

    for i in range(cycle):
        # print("num occupied", count_occupied(grid))
        positions = get_positions(grid, directions)
        new_grid = deepcopy(grid)
        for pos in positions:
            noccupied = get_occupied(grid, pos, directions)
            # print(pos, noccupied)
            if grid[pos] == "#" and not 2 <= noccupied <= 3:
                new_grid[pos] = "."
            elif grid[pos] == "." and noccupied == 3:
                new_grid[pos] = "#"
        grid = deepcopy(new_grid)
    # print(grid.keys())
    return count_occupied(grid)


def p2(inp):
    grid = defaultdict(lambda: ".")
    cycle = 6

    directions = get_directions()
    # initialise input
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            grid[(i, j, 0, 0)] = inp[j][i]

    for i in range(cycle):
        # print("num occupied", count_occupied(grid))
        positions = get_positions4d(grid, directions)
        new_grid = deepcopy(grid)
        for pos in positions:
            noccupied = get_occupied4d(grid, pos, directions)
            # print(pos, noccupied)
            if grid[pos] == "#" and not 2 <= noccupied <= 3:
                new_grid[pos] = "."
            elif grid[pos] == "." and noccupied == 3:
                new_grid[pos] = "#"
        grid = deepcopy(new_grid)
    # print(grid.keys())
    return count_occupied(grid)


inp = get_input()
print(p1(inp))
print(p2(inp))
