from utils import get_input


def play_game(nums, end):
    n = len(nums)

    nums_spoken = {nums[i]: i + 1 for i in range(n - 1)}

    next_last = nums[-1]
    for i in range(n - 1, end):
        last = next_last

        if last not in nums_spoken:
            # nums.append(0)
            next_last = 0
        else:
            diff = i + 1 - nums_spoken[last]
            # nums.append(diff)
            next_last = diff
        nums_spoken[last] = i + 1
    return last


def p1(inp):
    nums = list(map(int, inp[0].split(",")))
    return play_game(nums, 2020)


def p2(inp):
    nums = list(map(int, inp[0].split(",")))
    return play_game(nums, 30000000)


inp = get_input()
print(p1(inp))
# print(p2(inp))
