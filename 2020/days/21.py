from utils import get_input

import re


def p1(inp):
    ia = dict()
    ings = []
    potential = dict()
    for line in inp:
        if lm := re.match(r'([\w,\s]+) \(contains ([\w,\s]+)\)', line):
            inp_ingredients, inp_allergens = lm.groups()
            allergens = [x.strip() for x in inp_allergens.split(',')]
            ingredients = inp_ingredients.split(' ')
            for a in allergens:
                if a not in ia:
                    ia[a] = []
                ia[a].append(ingredients)
            ings.extend(ingredients)

    print(ia)
    for allergen, value in ia.items():
        pi = set(value[0])
        for i in value[1:]:
            pi = pi.intersection(set(i))
        potential[allergen] = pi
    defo = dict()
    while not all([True if len(x) == 1 else False for x in potential.values()]):
        for allergen in potential.keys():
            if len(potential[allergen]) == 1:
                pa = list(potential[allergen])[0]
                for a2 in potential.keys():
                    if a2 == allergen: continue
                    print(allergen, a2, potential)
                    potential[a2].discard(pa)

    potential = dict(sorted(potential.items()))
    aaas = set(list(x)[0] for x in potential.values())

    print(potential)
    print(aaas)
    no = [x for x in ings if x not in aaas]
    print(','.join(list(x)[0] for x in potential.values()))
    return len(no)


def p2(inp):
    pass


inp = get_input()
print(p1(inp))
print(p2(inp))
