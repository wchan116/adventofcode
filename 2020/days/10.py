from utils import get_input

def p1(inp):
    device = max(inp)
    outlet = 0
    one_jolt_diff = 0
    three_jolt_diff = 1

    inp.sort()
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i - 1]
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
    return one_jolt_diff * three_jolt_diff

def p2(inp):
    inp.sort()
    nums = set(inp)

    paths = [0] * len(inp)
    paths[0] = 1
    
    for i in range(len(inp)):
        try:
            if inp[i + 1] - inp[i] <= 3:
                paths[i + 1] += paths[i]
            if inp[i + 2] - inp[i] <= 3:
                paths[i + 2] += paths[i]
            if inp[i + 3] - inp[i] <= 3:
                paths[i + 3] += paths[i]
        except:
            continue

    return paths


inp = list(map(int, get_input()))
inp.append(0)
print(p1(inp))
print(p2(inp))