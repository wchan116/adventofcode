from utils import get_input

from copy import deepcopy
directions = {
    'e': lambda x, y, z: (x + 1, y, z - 1),
    'w': lambda x, y, z: (x - 1, y, z + 1),
    'ne': lambda x, y, z: (x + 1, y - 1, z),
    'nw': lambda x, y, z: (x, y - 1, z + 1),
    'se': lambda x, y, z: (x, y + 1, z - 1),
    'sw': lambda x, y, z: (x - 1, y + 1, z)
}


def p1(inp):
    instructions = []
    for line in inp:
        i = 0
        li = []
        while i < len(line):
            if (line[i] == 's' or line[i] == 'n') and (line[i + 1] != 's' or line[i + 1] != 'n'):
                li.append(line[i] + line[i + 1])
                i += 1
            else:
                li.append(line[i])
            i += 1
        instructions.append(li)
    visited = set()
    # print(instructions)
    for i in instructions:
        pos = (0, 0, 0)
        for l in i:
            pos = directions[l](pos[0], pos[1], pos[2])

        if pos in visited:
            visited.remove(pos)
        else:
            visited.add(pos)
    return len(visited)


def p2(inp):
    instructions = []
    for line in inp:
        i = 0
        li = []
        while i < len(line):
            if (line[i] == 's' or line[i] == 'n') and (line[i + 1] != 's' or line[i + 1] != 'n'):
                li.append(line[i] + line[i + 1])
                i += 1
            else:
                li.append(line[i])
            i += 1
        instructions.append(li)
    all_tiles = dict()
    visited = set()
    max_x, max_y, max_z = 0, 0, 0
    min_x, min_y, min_z = 0, 0, 0
    for i in instructions:
        pos = (0, 0, 0)
        for l in i:
            pos = directions[l](pos[0], pos[1], pos[2])

        max_x = max(pos[0], max_x)
        max_y = max(pos[1], max_y)
        max_z = max(pos[2], max_z)
        min_x = min(pos[0], min_x)
        min_y = min(pos[1], min_y)
        min_z = min(pos[2], min_z)

        if pos in visited:
            all_tiles[pos] = 'white'
            visited.remove(pos)
        else:
            all_tiles[pos] = 'black'
            visited.add(pos)

    print(min_x, min_y, min_z)
    print(max_x, max_y, max_z)
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                if (x, y, z) not in all_tiles:
                    all_tiles[(x, y, z)] = 'white'
                    # all_tiles['white'].add((x, y, z))
    print(list(all_tiles.values()).count('black'))

    for i in range(100):
        new_tiles = deepcopy(all_tiles)
        for tile, colour in all_tiles.items():
            nadjacent = 0
            for d in directions.values():
                neighbour = d(*tile)
                if all_tiles.get(neighbour, 'white') == 'black':
                    nadjacent += 1
                elif neighbour not in all_tiles:
                    new_tiles[neighbour] = 'white'

            if colour == 'black' and (nadjacent == 0 or nadjacent > 2):
                new_tiles[tile] = 'white'
            elif colour == 'white' and (nadjacent == 2):
                new_tiles[tile] = 'black'
        if (i+1) % 10 == 0:
            print(f"round {i+1}", list(new_tiles.values()).count('black'))
        all_tiles = new_tiles
    return list(all_tiles.values()).count('black')


inp = get_input()
print(p1(inp))
print(p2(inp))
