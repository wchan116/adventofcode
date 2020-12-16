from utils import get_input

import re


def process_input(inp):
    ranges = {}

    my_tick = False
    near_tick = False

    my_tickets = []
    nearby_tickets = []

    for line in inp:
        if lm := re.match(r"([\w ]+): (\d+)\-(\d+) or (\d+)-(\d+)", line):
            field = lm.group(1)
            r1, r2, r3, r4 = map(int, lm.groups(0)[1:])
            ranges[field] = [(r1, r2), (r3, r4)]
        elif lm := re.match(r"your ticket:", line):
            my_tick = True
        elif my_tick:
            my_tickets = list(map(int, line.split(",")))
            my_tick = False
        elif lm := re.match(r"nearby tickets:", line):
            near_tick = True
        elif near_tick:
            nearby_tickets.append(list(map(int, line.split(","))))
    return ranges, my_tickets, nearby_tickets


def p1(inp):
    ranges, _, nearby_tickets = process_input(inp)
    ranges = [r for sublist in list(ranges.values()) for r in sublist]
    return sum(get_error(ranges, ticket) for ticket in nearby_tickets)


def check_valid_ticket(ranges, ticket):
    x = [
        not all([True if not s <= val <= e else False for s, e in ranges])
        for val in ticket
    ]
    return all(x)


def get_error(ranges, ticket):
    return sum(
        [min([val if not s <= val <= e else 0 for s, e in ranges]) for val in ticket]
    )


def p2(inp):
    ranges, my_tickets, nearby_tickets = process_input(inp)
    flat_ranges = [r for sublist in list(ranges.values()) for r in sublist]

    fields = set(ranges.keys())
    f = [set() for _ in range(len(ranges.keys()))]

    valid_tickets = []
    for ticket in nearby_tickets:
        if check_valid_ticket(flat_ranges, ticket):
            valid_tickets.append(ticket)

    cols = [
        [ticket[i] for ticket in valid_tickets] for i in range(len(valid_tickets[0]))
    ]

    for i in range(len(cols)):
        potential = []
        for v in cols[i]:
            in_range = set()
            for r, l in ranges.items():
                r1, r2 = l[0], l[1]
                r1_s, r1_e = r1
                r2_s, r2_e = r2

                if r1_s <= v <= r1_e or r2_s <= v <= r2_e:
                    in_range.add(r)
            potential.append(in_range)
        f[i] = set.intersection(*potential)
    while fields:
        for i in range(len(cols)):
            if len(f[i]) == 1:
                f[i] = list(f[i])[0]
                fields.remove(f[i])
        for i in range(len(cols)):
            if isinstance(f[i], set):
                f[i] = f[i].intersection(fields)
    indices = []
    for i in range(len(f)):
        if f[i].startswith("departure"):
            indices.append(i)
    print(indices)
    prod = 1

    print(my_tickets)
    for idx in indices:
        print(my_tickets[idx])
        prod *= my_tickets[idx]

    return prod


inp = get_input()
print(p1(inp))
print(p2(inp))
