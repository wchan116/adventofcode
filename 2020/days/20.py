from utils import get_input
import re
import functools

def transpose(matrix):
    list_matrix = [list(x) for x in matrix]
    transposed = list(map(list, zip(*list_matrix)))
    return [''.join(x) for x in transposed]

def reversed_matrix(matrix):
    return [x[::-1] for x in matrix]


def p1(inp):
    tiles = {}
    current_tile = None
    for line in inp:
        if lm := re.match(r'Tile (\d+)', line):
            current_tile = int(lm.group(1))
            tiles[current_tile] = []
        elif line == '':
            continue
        else:
            tiles[current_tile].append(line)

    corner_tiles = []
    for (tile_num, tile) in tiles.items():
        num_adjacent = 0
        for (other_tile_num, other_tile) in tiles.items():
            if tile_num == other_tile_num:
                continue

            n = len(tile) - 1
            indexes = [0, n]
            reversed_tile = reversed_matrix(tile)
            reversed_other = reversed_matrix(other_tile)
            transposed = transpose(tile)
            other_transposed = transpose(other_tile)
            reverse_transposed = reversed_matrix(transposed)
            reverse_other_transposed = reversed_matrix(other_transposed)

            matrices = [reversed_tile, reversed_other, other_transposed, reverse_transposed, reverse_other_transposed]
            adjacent = False
            for index in indexes:
                for matrix in matrices:
                    if tile[index] == matrix[0] or tile[index] == matrix[n]:
                        adjacent = True
                    elif reversed_tile != matrix and (reversed_tile[index] == matrix[0] or reversed_tile[index] == matrix[n]):
                        adjacent = True
                    elif transposed[index] == matrix[0] or transposed[index] == matrix[n]:
                        adjacent = True
                    elif reverse_transposed != matrix and (reverse_transposed[index] == matrix[0] or reverse_transposed[index] == matrix[n]):
                        adjacent = True

            if adjacent:
                #print(tile_num, other_tile_num)
                num_adjacent += 1 

        #print(tile_num, num_adjacent)
        if num_adjacent == 2:
            corner_tiles.append(tile_num)
    print(corner_tiles)
    return functools.reduce(lambda x, y: x * y, corner_tiles)


def p2(inp):
    pass


inp = get_input()
print(p1(inp))
print(p2(inp))
