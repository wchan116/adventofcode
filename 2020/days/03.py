def p1(inp, slope):
    r, d = slope
    width = len(inp[0])
    height = len(inp)
    x, y = (0, 0)
    trees = 0
    while y < height:
        x = (x + r) % width
        y += d
        if y >= height: break
        if inp[y][x] == '#':
            trees += 1
    return trees


def p2(inp):
    return p1(inp, (1, 1)) * p1(inp, (3, 1)) * p1(inp, (5, 1)) * p1(inp, (7, 1)) * p1(inp, (1, 2))

with open('input/03.in') as f:
    inp = [l.strip() for l in f.readlines()]

print(p1(inp, (3, 1)))
print(p2(inp))
