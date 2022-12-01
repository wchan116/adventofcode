from utils import get_input

import numpy as np

def p1(inp):
    grid = np.matrix([list(map(int, x)) for x in inp])
    tp = grid.transpose()
    msb = ['1' if r.tolist()[0].count(1) > r.tolist()[0].count(0) else '0' for r in tp]
    lsb = [str(int(not int(x))) for x in msb]
    return int(''.join(msb), 2) * int(''.join(lsb), 2)

def get_rating(inp, best_pred):
    keep = inp
    for i in range(len(inp[0])):
        if len(keep) <= 1:
            break
        grid = np.matrix([list(x) for x in keep])
        tp = grid.transpose()
        row = tp[i].tolist()[0]
        ones = row.count('1')
        zeroes = row.count('0')
        best = best_pred(ones, zeroes)
        keep = [x for x in keep if x[i] == best]
    return int(keep[0], 2)

def p2(inp):
    oxygen_generator_rating = get_rating(inp, lambda x, y: '1' if x >= y else "0")
    co2_scrubber_rating = get_rating(inp, lambda x, y: '1' if x < y else "0")

    return oxygen_generator_rating * co2_scrubber_rating


inp = get_input()
print(p1(inp))
print(p2(inp))
