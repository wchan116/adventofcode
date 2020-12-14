from utils import get_input


def bin_partition(string, lo, hi, X, Y):
    for c in string[:-1]:
        mid = (lo + hi) // 2

        if c == X:
            hi = mid
        elif c == Y:
            lo = mid + 1
    if string[-1] == X:
        return lo
    elif string[-1] == Y:
        return hi


def p1(inp):
    max_sid = -float("inf")
    for line in inp:
        row = bin_partition(line[0:7], 0, 127, "F", "B")
        col = bin_partition(line[7:], 0, 7, "L", "R")

        max_sid = max(max_sid, (row * 8) + col)
    return max_sid


def p2(inp):
    sids = set()
    for line in inp:
        row = bin_partition(line[0:7], 0, 127, "F", "B")
        col = bin_partition(line[7:], 0, 7, "L", "R")

        sids.add((row * 8) + col)

    lo = min(sids)
    hi = max(sids)
    # print(lo, hi)
    for i in range(lo, lo + 8):
        sids.remove(i)
    for i in range(hi, hi - 8, -1):
        sids.remove(i)
    potential_sids = set(range(lo + 8, hi - 8 + 1))
    return potential_sids.difference(sids)


inp = get_input()
print(p1(inp))
print(p2(inp))
