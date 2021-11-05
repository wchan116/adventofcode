from utils import get_input

import re


def is_valid(rules, rule):
    if rules[rule]['status']:
        return rules[rule]['data']
    final = "("

    for r in rules[rule]['data']:
        for num in r:
            s = is_valid(rules, num)
            final += s
        if r != rules[rule]['data'][-1]:
            final += "|"
    final += ")"
    return final


def p1(inp):
    rules = {}
    messages = []

    for line in inp:
        if lm := re.match(r'^(\d+): "(\w+)"$', line):
            rule_num = int(lm.group(1))
            rule = lm.group(2)
            rules[rule_num] = dict()
            rules[rule_num]['status'] = True
            rules[rule_num]['data'] = rule
        elif lm := re.match(r"^(\d+): (.*)$", line):
            rule_num = int(lm.group(1))
            rules[rule_num] = dict()
            rule = [
                list(map(int, filter(lambda x: x != "", r.split(" "))))
                for r in lm.group(2).split("|")
            ]
            rules[rule_num]['status'] = False
            rules[rule_num]['data'] = rule
        elif lm := re.match(r"^(\w+)$", line):
            messages.append(line)
    # print(rules)
    regex = f"^{is_valid(rules, 0)}$"
    return sum(1 for msg in messages if re.match(regex, msg))


def p2(inp):
    pass


inp = get_input()
print(p1(inp))
print(p2(inp))
