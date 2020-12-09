from utils import get_input

from collections import deque

def check_sum_exists(window, target):
    ht = {}
    for i in range(len(window)):
        ht[window[i]] = i
    
    for i in range(len(window)):
        if target - window[i] in ht and i != ht[target - window[i]]:
            return True
    return False

def p1(inp):
    preamble = 25 
    window = deque(maxlen=preamble)

    for i in range(preamble):
        window.append(inp[i])

    for num in inp[preamble:]:
        if not check_sum_exists(window, num):
            return num
        window.append(num)
    return -1


def p2(inp):
    invalid_num = p1(inp)
    s = 0
    cont_set = []
    for num in inp:
        if num == invalid_num:
            s = 0
            cont_set = []
        s += num
        cont_set.append(num)
        if s > invalid_num:
            while s > invalid_num:
                s -= cont_set[0]
                cont_set.pop(0)
        if s == invalid_num:
            break
    return min(cont_set) + max(cont_set)


inp = list(map(int, get_input()))
print(p1(inp))
print(p2(inp))