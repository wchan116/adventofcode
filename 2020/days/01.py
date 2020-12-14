from utils import get_input


def p1(inp):
    n = len(inp)
    ht = {}

    for i in range(n):
        ht[inp[i]] = i

    for i in range(n):
        if 2020 - inp[i] in ht and i != ht[2020 - inp[i]]:
            return inp[i] * (2020 - inp[i])

    return -1


def p2(inp):
    n = len(inp)
    ht = {}

    for i in range(n):
        ht[inp[i]] = i

    for i in range(n):
        target = 2020 - inp[i]

        for j in range(1, n):
            if target - inp[j] in ht:
                return inp[i] * inp[j] * (target - inp[j])
    return -1


inp = list(map(int, get_input()))
print(p1(inp))
print(p2(inp))
