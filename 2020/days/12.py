from utils import get_input

import re
import math

directions = {0: "E", 1: "N", 2: "W", 3: "S"}


def p1(inp):
    ship_dir = 0
    ship_pos = [0, 0]

    for line in inp:
        lm = re.match(r"(\w)(\d+)", line)
        action = lm.group(1)
        value = int(lm.group(2))

        if action in {"N", "S", "E", "W"}:
            ship_pos = move_in_dir(ship_pos, action, value)
        elif action == "L":
            ship_dir = (((ship_dir * 90) + value) % 360) // 90
        elif action == "R":
            ship_dir = (((ship_dir * 90) - value) % 360) // 90
        elif action == "F":
            ship_pos = move_in_dir(ship_pos, directions[ship_dir], value)

    return abs(ship_pos[0]) + abs(ship_pos[1])


def move_in_dir(pos, dr, value):
    new_pos = pos
    if dr == "N":
        new_pos[1] += value
    elif dr == "S":
        new_pos[1] -= value
    elif dr == "E":
        new_pos[0] += value
    elif dr == "W":
        new_pos[0] -= value
    return new_pos


def p2(inp):
    ship_pos = [0, 0]
    waypoint_pos = [10, 1]

    for line in inp:
        lm = re.match(r"(\w)(\d+)", line)
        action = lm.group(1)
        value = int(lm.group(2))

        if action in {"N", "S", "E", "W"}:
            waypoint_pos = move_in_dir(waypoint_pos, action, value)
        elif action == "L":
            waypoint_pos = rotate_point(waypoint_pos, math.radians(value))
        elif action == "R":
            waypoint_pos = rotate_point(waypoint_pos, -math.radians(value))
        elif action == "F":
            ship_pos[0] += value * waypoint_pos[0]
            ship_pos[1] += value * waypoint_pos[1]
        print(waypoint_pos, ship_pos)

    return abs(ship_pos[0]) + abs(ship_pos[1])


def rotate_point(pos, value):
    new_pos = [0, 0]
    new_pos[0] = round(math.cos(value) * pos[0] - math.sin(value) * pos[1])
    new_pos[1] = round(math.sin(value) * pos[0] + math.cos(value) * pos[1])

    return new_pos


inp = get_input()
print(p1(inp))
print(p2(inp))
