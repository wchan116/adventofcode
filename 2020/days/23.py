from utils import get_input


def play_game(inp, rounds, extra=0):
    input = [int(x) for x in inp]
    cups = [0 for _ in range(len(input) + 1)]

    for i in range(1, len(input) + 1):
        cups[i] = input[(input.index(i) + 1) % len(input)]
    if extra:
        initial = traverse(cups, input[0])
        cups[initial[-1]] = max(input) + 1
        cups.extend([i + 1 for i in range(max(input)+1, extra)])
        cups[-1] = input[0]

    n = len(cups) - 1
    curr = input[0]

    for _ in range(rounds):
        three_cups = [cups[curr], cups[cups[curr]], cups[cups[cups[curr]]]]
        dest = curr - 1
        if dest < 1:
            dest = n
        while dest in three_cups:
            dest -= 1
            if dest < 1:
                dest = n

        next_cup = cups[cups[cups[cups[curr]]]]
        next_dest = cups[dest]

        # replace 3 cups after dest cup
        cups[dest] = cups[curr]
        cups[three_cups[2]] = next_dest
        cups[curr] = next_cup

        curr = cups[curr]

    return cups


def p1(inp):
    cups = play_game(inp, 100)
    ordered_cups = traverse(cups, 1)
    return ''.join([str(x) for x in ordered_cups][1:])


def traverse(l, start):
    visited = set()
    path = list()
    curr = start
    while True:
        if curr in visited: break
        visited.add(curr)
        path.append(curr)
        curr = l[curr]
    return path


def p2(inp):
    cups = play_game(inp, 10_000_000, 1_000_001)
    return cups[1] * cups[cups[1]]


inp = get_input()[0]
print(p1(inp))
print(p2(inp))
