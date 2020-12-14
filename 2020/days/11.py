from utils import get_input

from copy import deepcopy

directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}


def bfs(seats, start, end, direction):
    q = [start]
    seen = set()

    while q:
        curr = q.pop(0)
        x, y = curr

        if seats[x][y] != end and curr != start:
            return x, y

        seen.add(curr)

        x_dir, y_dir = direction
        nb = (x + x_dir, y + y_dir)
        if 0 <= x + x_dir < len(seats) and 0 <= y + y_dir < len(seats[0]):
            if nb not in seen:
                q.append(nb)
    return None


def get_neighbours(seats, start, end=None):
    neighbours = [bfs(seats, start, end, d) for d in directions]
    return list(filter(lambda x: x is not None, neighbours))


def find_seats(seats, nvisible, end=None):
    new_copy = deepcopy(seats)
    prev = deepcopy(new_copy)

    neighbours = {
        (i, j): get_neighbours(new_copy, (i, j), end)
        for i in range(len(inp))
        for j in range(len(inp[0]))
    }

    while True:
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if prev[i][j] == ".":
                    continue
                occupied = [
                    True if prev[x][y] == "#" else False for x, y in neighbours[(i, j)]
                ]
                if prev[i][j] == "L" and occupied.count(True) == 0:
                    new_copy[i][j] = "#"
                elif prev[i][j] == "#" and occupied.count(True) >= nvisible:
                    new_copy[i][j] = "L"
        if new_copy == prev:
            break
        prev = deepcopy(new_copy)
    return sum(x.count("#") for x in new_copy)


def p1(inp):
    return find_seats(inp, 4)


def p2(inp):
    return find_seats(inp, 5, ".")


inp = [list(i) for i in get_input()]
print(p1(inp))
print(p2(inp))
