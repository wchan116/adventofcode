from utils import get_input

def calc_pos(inp, commands):
    hori, vert, aim = 0, 0, 0
    for line in inp:
        direction, steps = line.split(' ')
        steps = int(steps)

        hori, vert, aim = commands[direction](hori, vert, aim, steps)
    return hori * vert

def p1(inp):
    commands = {
        'forward': lambda h, v, a, x: (h + x, v, 0),
        'down': lambda h, v, a, x: (h, v + x, 0),
        'up': lambda h, v, a, x: (h, v - x, 0)
    }
    return calc_pos(inp, commands)

def p2(inp):
    commands = {
        'forward': lambda h, v, a, x: (h + x, v + a * x, a),
        'down': lambda h, v, a, x: (h, v, a + x),
        'up': lambda h, v, a, x: (h, v, a - x)
    }
    return calc_pos(inp, commands)
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
