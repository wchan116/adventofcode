from utils import get_input

import re
from itertools import combinations


def p1(inp):
    memory = {}
    for line in inp:
        if line.startswith("mask"):
            lm = re.match(r"mask = ([X10]{36})", line)
            mask = lm.group(1)

            keep_bits = mask.replace("1", "0").replace("X", "1")
            overwrite_bits = mask.replace("X", "0")
        elif line.startswith("mem"):
            lm = re.match(r"mem\[(\d+)\] = (\d+)", line)
            mem_loc, val = map(int, lm.groups(0))

            memory[mem_loc] = (val & int(keep_bits, 2)) | int(overwrite_bits, 2)
    return sum(memory.values())


def p2(inp):
    memory = {}
    for line in inp:
        if line.startswith("mask"):
            lm = re.match(r"mask = ([X10]{36})", line)
            mask = lm.group(1)

        elif line.startswith("mem"):
            lm = re.match(r"mem\[(\d+)\] = (\d+)", line)
            mem_loc, val = map(int, lm.groups(0))

            mem_as_bin = bin(mem_loc)[2:]
            mem_as_bin = ("0" * (36 - len(mem_as_bin))) + mem_as_bin

            res = [mem_as_bin[i] if mask[i] == "0" else mask[i] for i in range(36)]
            n_x = res.count("X")
            # combos = {x for x in combinations(n_x * "01", n_x)}
            combos = {format(x, f"#0{n_x+2}b")[2:] for x in range(2 ** n_x - 1)}
            for c in combos:
                c = list(c)
                addr = [c.pop(0) if res[i] == "X" else res[i] for i in range(36)]
                addr = int("".join(addr))
                memory[addr] = val

    return sum(memory.values())


inp = get_input()
print(p1(inp))
print(p2(inp))
