from utils import get_input

from copy import deepcopy

def print_seats(seats):
    s = [''.join(x) for x in seats]
    print(s)

def p1(inp):
    new_copy = deepcopy(inp)
    prev = deepcopy(new_copy)

    while True:
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                occupied = check_adjacent(prev, i, j)
                #print(occupied)
                if prev[i][j] == 'L' and occupied.count(True) == 0:
                    new_copy[i][j] = '#'
                elif prev[i][j] == '#' and occupied.count(True) >= 4:
                    new_copy[i][j] = 'L'
        #print_seats(new_copy)
        if new_copy == prev:
            break
        prev = deepcopy(new_copy)
    return sum(x.count('#') for x in new_copy)
        
    #print_seats(new_copy)

def check_adjacent(seats, i, j):
    adj_list = []
    if i-1 >= 0:
        adj_list.append(seats[i-1][j])
        if j-1 >= 0:
            adj_list.append(seats[i-1][j-1])
        if j+1 < len(seats[0]):
            adj_list.append(seats[i-1][j+1])
    if i+1 < len(seats):
        adj_list.append(seats[i+1][j])
        if j-1 >= 0:
            adj_list.append(seats[i+1][j-1])
        if j+1 < len(seats[0]):
            adj_list.append(seats[i+1][j+1])
    if j-1 >= 0:
        adj_list.append(seats[i][j-1])
    if j+1 < len(seats[0]):
        adj_list.append(seats[i][j+1])
    occupied = [True if x == '#' else False for x in adj_list]
    return occupied 

def bfs(seats, start, direction):
    q = [start]
    seen = set()

    while q:
        curr = q.pop(0)
        x, y = curr

        if seats[x][y] != '.' and curr != start:
            return x, y 
        
        seen.add(curr)

        x_dir, y_dir = direction
        nb = (x + x_dir, y + y_dir)
        if 0 <= x + x_dir < len(seats) and 0 <= y + y_dir < len(seats[0]):
            if nb not in seen:
                q.append(nb)
    return None

        
def get_neighbours(seats, start):
    neighbours = []
    neighbours.append(bfs(seats, start, (-1, -1))) # NW
    neighbours.append(bfs(seats, start, (-1, 0)))  # N
    neighbours.append(bfs(seats, start, (-1, 1)))  # NE
    neighbours.append(bfs(seats, start, (0, -1)))  # W
    neighbours.append(bfs(seats, start, (0, 1)))   # E
    neighbours.append(bfs(seats, start, (1, -1)))  # SW
    neighbours.append(bfs(seats, start, (1, 0)))   # S
    neighbours.append(bfs(seats, start, (1, 1)))   # SE

    return list(filter(lambda x : x is not None, neighbours))

def p2(inp):
    new_copy = deepcopy(inp)
    prev = deepcopy(new_copy)
    
    neighbours = {}
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            neighbours[(i, j)] = get_neighbours(new_copy, (i, j))

    while True:
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                if prev[i][j] == '.': continue
                occupied = [True if prev[x][y] == '#' else False for x, y in neighbours[(i, j)]]
                if prev[i][j] == 'L' and occupied.count(True) == 0:
                    new_copy[i][j] = '#'
                elif prev[i][j] == '#' and occupied.count(True) >= 5:
                    new_copy[i][j] = 'L'
        if new_copy == prev:
            break
        prev = deepcopy(new_copy)
    return sum(x.count('#') for x in new_copy)


inp = [list(i) for i in get_input()]
print(p1(inp))
print(p2(inp))