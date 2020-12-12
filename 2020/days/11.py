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

def check_first_seen(seats, i, j):
    adj_list = []
    # north west
    x, y = i, j
    while x >= 0 and y >= 0:
        if (x == i and y == j) or seats[x][y] == '.':
            x -= 1
            y -= 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x -= 1
        y -= 1

    # north
    x, y = i, j
    while x >= 0:
        if x == i or seats[x][y] == '.':
            x -= 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break

        x -= 1
    
    # north east
    x, y = i, j
    while x >= 0 and y < len(seats[0]):
        if (x == i and y == j) or seats[x][y] == '.':
            x -= 1
            y += 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x -= 1
        y += 1

    # north east
    x, y = i, j
    while x >= 0 and y < len(seats[0]):
        if (x == i and y == j) or seats[x][y] == '.':
            x -= 1
            y += 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x -= 1
        y += 1

    # west
    x, y = i, j
    while y >= 0:
        if (x == i and y == j) or seats[x][y] == '.':
            y -= 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        y -= 1

    # east
    x, y = i, j
    while y < len(seats[0]):
        if (x == i and y == j) or seats[x][y] == '.':
            y += 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        y += 1

    # south west
    x, y = i, j
    while x < len(seats) and y >= 0:
        if (x == i and y == j) or seats[x][y] == '.':
            x += 1
            y -= 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x += 1
        y -= 1

    # south 
    x, y = i, j
    while x < len(seats):
        if (x == i and y == j) or seats[x][y] == '.':
            x += 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x += 1

    # south east
    x, y = i, j
    while x < len(seats) and y < len(seats[0]):
        if (x == i and y == j) or seats[x][y] == '.':
            x += 1
            y += 1
            continue
        if seats[x][y] != '.':
            adj_list.append(seats[x][y])
            break
        x += 1
        y += 1

    return adj_list

def p2(inp):
    new_copy = deepcopy(inp)
    prev = deepcopy(new_copy)

    while True:
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                if prev[i][j] == '.': continue
                occupied = check_first_seen(prev, i, j)
                print(occupied)
                if prev[i][j] == 'L' and occupied.count(True) == 0:
                    new_copy[i][j] = '#'
                elif prev[i][j] == '#' and occupied.count(True) >= 4:
                    new_copy[i][j] = 'L'
        #print_seats(new_copy)
        break
        if new_copy == prev:
            break
        prev = deepcopy(new_copy)
    return sum(x.count('#') for x in new_copy)

inp = [list(i) for i in get_input()]
print(p1(inp))
print(p2(inp))