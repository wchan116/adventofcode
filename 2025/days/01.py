import re
from math import ceil, floor

instructions = []

with open("../input/01.in") as f:
    instructions = f.readlines()


MAX_DIAL = 100


def p1():
    dial = 50

    zeroes = 0

    for instr in instructions:
        if lm := re.match(r"(L|R)(\d+)", instr):
            num = int(lm.groups()[1])
            if lm.groups()[0] == "L":
                dial = (dial - num) % MAX_DIAL
            elif lm.groups()[0] == "R":
                dial = (dial + num) % MAX_DIAL
        if dial == 0:
            zeroes += 1

    return zeroes


def p2():
    dial = 50

    zeroes = 0

    for instr in instructions:
        if lm := re.match(r"(L|R)(\d+)", instr):
            num = int(lm.groups()[1])
            print(lm.groups())
            if lm.groups()[0] == "L":
                quotient = num / MAX_DIAL
                remainder = (dial - num) % MAX_DIAL

                if remainder > dial or remainder == 0:
                    zeroes += ceil(quotient)
                    if dial == 0:
                        zeroes -= 1
                elif remainder < dial and floor(quotient) > 0:
                    zeroes += floor(quotient)
                dial = remainder
            elif lm.groups()[0] == "R":
                quotient = num / MAX_DIAL
                remainder = (dial + num) % MAX_DIAL

                if remainder < dial or remainder == 0:
                    zeroes += ceil(quotient)
                    if dial == 0:
                        zeroes -= 1
                elif remainder > dial and floor(quotient) > 0:
                    zeroes += floor(quotient)
                dial = remainder

    return zeroes


print(p1())
print(p2())
