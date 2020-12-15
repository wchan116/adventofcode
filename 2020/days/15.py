from utils import get_input


def p1(inp, end):
    nums = list(map(int, inp[0].split(",")))
    n = len(nums)

    nums_spoken = {nums[i]: i + 1 for i in range(n - 1)}

    for i in range(n - 1, end):
        last = nums[-1]

        if last not in nums_spoken:
            nums.append(0)
        else:
            diff = i + 1 - nums_spoken[last]
            nums.append(diff)
        nums_spoken[last] = i + 1
    return nums[end - 1]


def p2(inp, end):
    return p1(inp, end)


inp = get_input()
print(p1(inp, 2020))
print(p2(inp, 30000000))
