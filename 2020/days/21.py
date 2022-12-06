from utils import get_input

import re


def get_allergen_ingredients(inp):
    allergen_ingredients = dict()
    all_ingredients = []
    for line in inp:
        if lm := re.match(r'([\w,\s]+) \(contains ([\w,\s]+)\)', line):
            inp_ingredients, inp_allergens = lm.groups()
            allergens = [x.strip() for x in inp_allergens.split(',')]
            ingredients = inp_ingredients.split(' ')
            for a in allergens:
                if a not in allergen_ingredients:
                    allergen_ingredients[a] = set(ingredients)
                else:
                    allergen_ingredients[a] = allergen_ingredients[a].intersection(set(ingredients))
            all_ingredients.extend(ingredients)

    # since we know theres 1 to 1 mapping from allergens to ingredients
    # keep looping until we find a match
    while not all([True if len(x) == 1 else False for x in allergen_ingredients.values()]):
        for allergen in allergen_ingredients.keys():
            if len(allergen_ingredients[allergen]) == 1:
                ingredient = list(allergen_ingredients[allergen])[0]
                for other in allergen_ingredients.keys():
                    if other == allergen: continue
                    allergen_ingredients[other].discard(ingredient)

    allergen_ingredients = dict(sorted(allergen_ingredients.items()))
    return allergen_ingredients, all_ingredients


def p1(inp):
    allergen_ingredients, all_ingredients = get_allergen_ingredients(inp)
    allergens = set(list(x)[0] for x in allergen_ingredients.values())

    return len([x for x in all_ingredients if x not in allergens])


def p2(inp):
    allergen_ingredients, all_ingredients = get_allergen_ingredients(inp)
    return ','.join(list(x)[0] for x in allergen_ingredients.values())


inp = get_input()
print(p1(inp))
print(p2(inp))
