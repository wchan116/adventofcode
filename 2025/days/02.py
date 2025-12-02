id_ranges = []
with open("input/02.in") as f:
    id_ranges = [x for x in f.readline().strip().split(",") if x]


def p1():
    invalid = 0
    for idr in id_ranges:
        first, second = idr.split("-")

        for i in range(int(first), int(second) + 1):
            if len(str(i)) % 2 == 1:
                continue
            elif str(i)[: len(str(i)) // 2] == str(i)[len(str(i)) // 2 :]:
                invalid += i
    return invalid


def p2():
    invalid = 0
    for idr in id_ranges:
        first, second = idr.split("-")

        for i in range(int(first), int(second) + 1):
            for j in range(len(str(i)) - 1):
                window = str(i)[: j + 1]
                if window * (len(str(i)) // len(window)) == str(i):
                    invalid += i
                    break

    return invalid


print(p1())
print(p2())
