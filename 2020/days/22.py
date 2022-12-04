from utils import get_input

from copy import deepcopy

def winning(decks, winner):
    loser = int(not winner)
    decks[winner].append(decks[winner][0])
    decks[winner].append(decks[loser][0])
    decks[winner].pop(0)
    decks[loser].pop(0)


def get_score(decks):
    score = 0
    winner = decks[0] if decks[0] else decks[1]
    i = len(winner)
    for card in winner:
        score += card * i
        i -= 1
    return score


def p1(decks):
    while decks[0] and decks[1]:
        if decks[0][0] > decks[1][0]:
            winning(decks, 0)
        elif decks[1][0] > decks[0][0]:
            winning(decks, 1)
    return get_score(decks)


def play_game(decks):
    history = set()
    i = 0
    while decks[0] and decks[1]:
        h = tuple(tuple(x) for x in decks)
        if h in history:
            winning(decks, 0)
            return 0

        # print(x)
        history.add(h)
        w = None
        if decks[0][0] < len(decks[0]) and decks[1][0] < len(decks[1]):
            w = play_game([decks[0][1:decks[0][0] + 1], decks[1][1:decks[1][0] + 1]])
        if w == 0 or (w is None and decks[0][0] > decks[1][0]):
            winning(decks, 0)
        elif w == 1 or (w is None and decks[1][0] > decks[0][0]):
            winning(decks, 1)
        i += 1
    return 0 if decks[0] else 1


def p2(decks):
    play_game(decks)
    return get_score(decks)


inp = get_input()
decks = [[], []]
player = None
for line in inp:
    if line == "Player 1:":
        player = 0
    elif line == "Player 2:":
        player = 1
    elif line == "":
        continue
    else:
        decks[player].append(int(line))

print(p1(deepcopy(decks)))
print(p2(deepcopy(decks)))
