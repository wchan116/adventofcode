
with open('input/06.in') as f:
    inp = [l for l in f.readlines()]

def p1(inp):
    questions = set()
    answers = 0
    for line in inp:
        if line == '\n':
            #print(questions)
            answers += len(questions)
            questions = set()
        questions = questions.union(set(list(line.strip())))
    answers += len(questions)
    return answers

def p2(inp):
    answers = 0
    questions = []
    for line in inp:
        if line == '\n':
            answers += len(set.intersection(*questions))
            questions = []
            continue

        curr_grp = set(list(line.strip()))
        questions.append(curr_grp)
    answers += len(set.intersection(*questions))

    return answers

print(p1(inp))
print(p2(inp))
