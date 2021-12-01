from utils import get_input


def p1(inp):
    larger = 0
    prev = int(inp[0])
    for line in inp[1:]:
        num = int(line)
        if num > prev:
            larger += 1
        prev = num
    return larger

def get_window_sum(arr, start):
    if start + 3 > len(arr):
        return 0 
    return sum(arr[start: start+3])

def p2(inp):
    inp = [int(x) for x in inp]
    larger = 0
    prev = get_window_sum(inp, 0)
    for i, line in enumerate(inp[1:]):
        s = get_window_sum(inp, i)
        if s > prev:
            larger += 1
        prev = s
    return larger


inp = get_input()
print(p1(inp))
print(p2(inp))
