def p1(bags):
    return sum(1 for color in bags.keys() if color != "shiny gold" and bfs(bags, color))


def bfs(bags, start):
    q = [start]
    seen = set()

    while q:
        curr = q.pop(0)

        if curr == "shiny gold":
            return True

        seen.add(curr)
        for nb in bags[curr]:
            if nb not in seen:
                q.append(nb)
    return False


def p2(bags):
    return dfs(bags, "shiny gold")


def dfs(bags, start):
    s = [start]
    nbags = 0

    while s:
        curr = s.pop()

        nbags += 1
        for nb, n in bags[curr].items():
            for i in range(n):
                s.append(nb)
    return nbags - 1


with open("input/07.in") as f:
    inp = [l.replace(",", " ").replace(".", " ").strip() for l in f.readlines()]
    bags = {}

    for line in inp:
        line_split = line.split()
        container = None
        for idx, word in enumerate(line_split):
            if word in {"bag", "bags"}:
                color = line_split[idx - 2] + " " + line_split[idx - 1]
                if color == "no other":
                    continue
                if container:
                    nbags = int(line_split[idx - 3])
                    bags[container][color] = nbags
                else:
                    container = color
                    bags[container] = {}

print(p1(bags))
print(p2(bags))
