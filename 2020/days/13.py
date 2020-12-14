from functools import reduce
from operator import mul


def p1(s_time, buses):
    buses = [int(x.strip()) for x in buses.split(",") if x != "x"]
    c_time = float("inf")
    c_bus = -1
    for bus in buses:
        div = round(s_time / bus)
        d_time = div * bus
        # print(d_time)
        if d_time >= s_time and abs(d_time - s_time) < abs(c_time - s_time):
            c_time = d_time
            c_bus = bus
    return (c_time - s_time) * c_bus


def p2(s_time, buses):
    buses = [x.strip() for x in buses.split(",")]
    earliest = 0
    prod = reduce(mul, [int(x) for x in buses if x != "x"])

    for i in range(len(buses)):
        if buses[i] == "x":
            continue
        bus = int(buses[i])
        n_bar = prod // bus
        u = pow(n_bar, -1, bus)

        earliest += u * n_bar * -i
    return earliest % prod


with open("input/13.in") as f:
    dep_time = int(f.readline().strip())
    buses = f.readline()

print(p1(dep_time, buses))
print(p2(dep_time, buses))
