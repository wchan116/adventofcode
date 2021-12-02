from utils import get_input


def p1(inp):
    hori, vert= 0, 0
    for line in inp:
        direction, steps = line.split(' ')
        steps = int(steps)
        
        if direction == 'forward':
            hori += steps
        elif direction == 'down':
            vert += steps
        elif direction == 'up':
            vert -= steps
    return hori * vert



def p2(inp):
    hori, vert, aim = 0, 0, 0
    for line in inp:
        direction, steps = line.split(' ')
        steps = int(steps)
        
        if direction == 'forward':
            hori += steps
            vert += aim * steps
        elif direction == 'down':
            aim += steps
        elif direction == 'up':
            aim -= steps
    return hori * vert


inp = get_input()
print(p1(inp))
print(p2(inp))
