from utils import get_input


import re

operators = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
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
    return int(stack[0])


def solve2(expr):
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
    res = 0
    for line in inp:
        expr = list(
            filter(lambda x: x != " " and x != "", re.split(r"(\s+|\)|\()", line))
        )
        i = 0
        insert_start = []
        insert_end = []
        while i < len(expr):
            if expr[i] == "+":
                ignore = 0
                for j in range(i - 1, -1, -1):
                    if expr[j] == ")":
                        ignore += 1
                    elif expr[j] == "(":
                        ignore -= 1
                    if ignore == 0:
                        insert_start.append((j, "("))
                        break
                ignore = 0
                for j in range(i + 1, len(expr)):
                    if expr[j] == "(":
                        ignore += 1
                    elif expr[j] == ")":
                        ignore -= 1
                    if ignore == 0:
                        insert_end.append((j, ")"))
                        break
            i += 1
        print(insert_start)
        print(insert_end)
        inserted = insert_start + insert_end
        inserted = sorted(inserted)
        lt = lambda x: sum(1 for i in inserted if i < x)
        offset = 0
        for idx, c in inserted:
            if c == ")":
                expr.insert(idx + offset + 1, c)
            else:
                expr.insert(idx + offset, c)
            offset += 1
        # for idx_s, idx_e in zip(insert_start, insert_end):
        #     expr.insert(idx_s + lt(idx_s), "(")
        #     offset += 1
        #     expr.insert(idx_e + lt(idx_e) + 1, ")")
        #     offset += 1
        print(expr)
        # print(*enumerate(expr))
        # for i, idx in enumerate(insert_start):
        #     expr.insert(idx + i, "(")
        #     offset += 1
        # print(expr)
        # for i, idx in enumerate(insert_end):
        #     expr.insert(idx + i + (2 * i), ")")
        #     offset += 1
        # print(expr)
        res += solve(expr)

    return res


inp = get_input()
print(p1(inp))
print(p2(inp))
