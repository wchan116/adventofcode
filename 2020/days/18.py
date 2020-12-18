from utils import get_input


import re

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def solve(expr):
    stack = []
    op = ""
    i = 0
    while i < len(expr):
        ignore = 0
        # print(expr, stack)
        if expr[i] == "(":
            for j in range(i, len(expr)):
                if expr[j] == "(":
                    ignore += 1
                elif expr[j] == ")":
                    ignore -= 1
                    if ignore == 0:
                        res = solve(expr[i + 1 : j])
                        expr = expr[: i + 1] + [str(res)] + expr[j:]
                        # print(expr)
                        break
        elif expr[i].isnumeric():
            if op:
                res = int(stack.pop())
                res = operators[op](res, int(expr[i]))
                stack.append(res)
                op = ""
            else:
                stack.append(expr[i])
        elif expr[i] in operators.keys():
            op = expr[i]
        i += 1
    # print(stack[0])
    return stack[0]


def p1(inp):
    res = 0
    for line in inp:
        expr = list(
            filter(lambda x: x != " " and x != "", re.split(r"(\s+|\)|\()", line))
        )
        res += solve(expr)
    return res


def p2(inp):
    pass


inp = get_input()
print(p1(inp))
print(p2(inp))
