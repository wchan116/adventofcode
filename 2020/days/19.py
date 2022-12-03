from utils import get_input

import re


def is_valid(rules, rule, rec):
#     print(rec)
    if rec > 200:
        return ".*"
    if rules[rule]['status']:
        return rules[rule]['data']
    final = "("

    for r in rules[rule]['data']:
        for num in r:
            s = is_valid(rules, num, rec + 1)
            final += s
        if r != rules[rule]['data'][-1]:
            final += "|"
    final += ")"
    return final


def parse_input(inp):
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

    return rules, messages


def p1(inp):
    rules, messages = parse_input(inp)
    regex = f"^{is_valid(rules, 0, 0)}$"
    return sum(1 for msg in messages if re.match(regex, msg))


def p2(inp):
    rules, messages = parse_input(inp)
    rules[8] = {
        'status': False,
        'data': [[42], [42, 8]]
    }
    rules[11] = {
        'status': False,
        'data': [[42, 31], [42, 11, 31]]
    }
    regex = f"^{is_valid(rules, 0, 0)}$"
#     print(regex)
    return sum(1 for msg in messages if re.match(regex, msg))


inp = get_input()
print(p1(inp))
print(p2(inp))
