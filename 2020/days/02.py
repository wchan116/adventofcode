import re

def p1(inp):
    valid = 0
    for i in inp:
        lm = re.match(r'(\d+)-(\d+) (\w): (\w+)', i)
        if lm:
            lo_char, hi_char, letter, password = lm.groups(0)
            lo_char = int(lo_char)
            hi_char = int(hi_char)

            if lo_char <= password.count(letter) <= hi_char:
                valid += 1


    return valid

def p2(inp):
    valid = 0
    for i in inp:
        lm = re.match(r'(\d+)-(\d+) (\w): (\w+)', i)
        if lm:
            lo_char, hi_char, letter, password = lm.groups(0)
            lo_char = int(lo_char)
            hi_char = int(hi_char)

            if (password[lo_char - 1] == letter) + (password[hi_char - 1] == letter) == 1:
                valid += 1


    return valid

with open('input/02.in') as f:
    inp = [l.strip() for l in f.readlines()]

print(p1(inp))
print(p2(inp))
