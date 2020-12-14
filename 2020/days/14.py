from utils import get_input

import re
from itertools import combinations

def p1(inp):
    memory = {}
    for line in inp:
        if line.startswith('mask'):
            lm = re.match(r'mask = ([X10]{36})', line)
            mask = lm.group(1)
            keep_bits = mask.replace('1', '0').replace('X', '1')
            overwrite_bits = mask.replace('X', '0')
        elif line.startswith('mem'):
            lm = re.match(r'mem\[(\d+)\] = (\d+)', line)
            mem_loc, val = map(int, lm.groups(0))

            memory[mem_loc] = (val & int(keep_bits, 2)) | int(overwrite_bits, 2)
    return sum(memory.values())

def p2(inp):
    memory = {}
    for line in inp:
        if line.startswith('mask'):
            lm = re.match(r'mask = ([X10]{36})', line)
            mask = lm.group(1)

        elif line.startswith('mem'):
            lm = re.match(r'mem\[(\d+)\] = (\d+)', line)
            mem_loc, val = map(int, lm.groups(0))

            mem_as_bin = bin(mem_loc)[2:]
            mem_as_bin = ('0' * (36 - len(mem_as_bin))) + mem_as_bin
            
            res = ''
            for i in range(36):
                if mask[i] == '0':
                    res += mem_as_bin[i]
                elif mask[i] == '1':
                    res += '1'
                else:
                    res += 'X'
            n_x = res.count('X')
            floating = {x for x in combinations(n_x * '01', n_x)}
            copy_res = list(res)
            for fl in floating:
                for bit in fl:
                    copy_res[copy_res.index('X')] = bit
                copy_res = int(''.join(copy_res))
                memory[copy_res] = val
                copy_res = list(res)
                
    return sum(memory.values())

inp = get_input()
print(p1(inp))
print(p2(inp))