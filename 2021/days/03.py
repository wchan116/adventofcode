from utils import get_input

import numpy as np

def p1(inp):
    grid = np.matrix([list(map(int, x)) for x in inp])
    tp = grid.transpose()
    msb = ['1' if r.tolist()[0].count(1) > r.tolist()[0].count(0) else '0' for r in tp]
    lsb = [str(int(not int(x))) for x in msb]
    return int(''.join(msb), 2) * int(''.join(lsb), 2)

def get_rating(grid):
    while len(grid) > 1:
        ones = 0
        zeroes = 0
        for i in range(len(grid[0])):
            ones = 0
            zeroes = 0
            for j in range(len(grid)):
                if grid[j][i] == '1':
                    ones += 1
                else:
                    zeroes += 1
            to_remove = []
            if ones > zeroes:
                for x in grid:
                    if x[i] == '0':
                        to_remove.append(x)
            elif zeroes > ones:
                for x in grid:
                    if x[i] == '1':
                        to_remove.append(x)
            elif ones == zeroes:
                for x in grid:
                    if x[i] != '1':
                        to_remove.append(x)

            for rem in to_remove:
                grid.remove(rem)
            if len(grid) <= 1:
                break

def p2(inp):
    grid = np.matrix([list(x) for x in inp])
    tp = grid.transpose()
    for row in tp:
        r = row.tolist()[0]
        ones = r.count('1')
        zeroes = r.count('0')
    # grid = [x for x in inp]
    # while len(grid) > 1:
    #     ones = 0
    #     zeroes = 0
    #     for i in range(len(grid[0])):
    #         ones = 0
    #         zeroes = 0
    #         for j in range(len(grid)):
    #             if grid[j][i] == '1':
    #                 ones += 1
    #             else:
    #                 zeroes += 1
    #         to_remove = []
    #         if ones > zeroes:
    #             for x in grid:
    #                 if x[i] == '0':
    #                     to_remove.append(x)
    #         elif zeroes > ones:
    #             for x in grid:
    #                 if x[i] == '1':
    #                     to_remove.append(x)
    #         elif ones == zeroes:
    #             for x in grid:
    #                 if x[i] != '1':
    #                     to_remove.append(x)

    #         for rem in to_remove:
    #             grid.remove(rem)
    #         if len(grid) <= 1:
    #             break

    # oxygen_generator_rating = grid[0]
    # grid = [x for x in inp]
    # while len(grid) > 1:
    #     ones = 0
    #     zeroes = 0
    #     for i in range(len(grid[0])):
    #         ones = 0
    #         zeroes = 0
    #         for j in range(len(grid)):
    #             if grid[j][i] == '1':
    #                 ones += 1
    #             else:
    #                 zeroes += 1
    #         to_remove = []
    #         if ones > zeroes:
    #             for x in grid:
    #                 if x[i] == '1':
    #                     to_remove.append(x)
    #         elif zeroes > ones:
    #             for x in grid:
    #                 if x[i] == '0':
    #                     to_remove.append(x)
    #         elif ones == zeroes:
    #             for x in grid:
    #                 if x[i] != '0':
    #                     to_remove.append(x)

    #         for rem in to_remove:
    #             grid.remove(rem)
    #         if len(grid) <= 1:
    #             break
    # co2_scrubber_rating = grid[0]
    # return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


inp = get_input()
print(p1(inp))
print(p2(inp))
