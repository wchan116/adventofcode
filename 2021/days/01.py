from utils import get_input


def p1(inp):
    return find_larger(inp, get_window_sum)

def p2(inp):
    return find_larger(inp, get_window_sum, 3)

def get_window_sum(arr, start, additional):
    if start + additional > len(arr):
        return 0 
    return sum(arr[start: start+additional])

def find_larger(inp, sum_func, additional=1):
    inp = [int(x) for x in inp]
    return sum(1 for i in range(1, len(inp)) if sum_func(inp, i, additional) > sum_func(inp, i-1, additional))

inp = get_input()
print(p1(inp))
print(p2(inp))
