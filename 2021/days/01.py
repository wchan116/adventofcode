from utils import get_input


def p1(inp):
    return find_larger(inp, get_window_sum)

def p2(inp):
    return find_larger(inp, get_window_sum, 3)

def get_window_sum(arr, start, window_size):
    if start + window_size > len(arr):
        return 0 
    return sum(arr[start: start+window_size])

def find_larger(inp, sum_func, window_size=1):
    inp = [int(x) for x in inp]
    return sum(1 for i in range(1, len(inp)) if sum_func(inp, i, window_size) > sum_func(inp, i-1, window_size))

inp = get_input()
print(p1(inp))
print(p2(inp))
