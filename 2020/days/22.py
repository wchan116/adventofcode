from utils import get_input

from copy import deepcopy

def p1(inp):
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
    i = 0
    while decks[0] and decks[1]:
        print(f"round {i}")
        print(f"1 plays {decks[0][0]}")
        print(f"2 plays {decks[1][0]}")
        if decks[0][0] > decks[1][0]:
            print(f"1 wins")
            decks[0].append(decks[0][0])
            decks[0].append(decks[1][0])
            decks[0].pop(0)
            decks[1].pop(0)
        elif decks[1][0] > decks[0][0]:
            print(f"2 wins")
            decks[1].append(decks[1][0])
            decks[1].append(decks[0][0])
            decks[0].pop(0)
            decks[1].pop(0)
        i += 1
    score = 0
    winner = decks[0]
    if decks[1]: winner = decks[1]
    i = len(winner)
    for card in winner:
        score += card * i
        i -= 1
    print(decks)
    return score

def play_game(decks):
    history = set()
    i = 0
    while decks[0] and decks[1]:
        # print(f"round {i}")
        # print(decks)
        # print(f"1 plays {decks[0][0]}")
        # print(f"2 plays {decks[1][0]}")
        # print(f"history {history}")
        h = tuple(tuple(x) for x in decks)
        if h in history:
            # print(decks)
            # print(history)
            print(f"1 wins by history")
            decks[0].append(decks[0][0])
            decks[0].append(decks[1][0])
            decks[0].pop(0)
            decks[1].pop(0)
            return 0

        # print(x)
        history.add(h)
        w = None
        if decks[0][0] < len(decks[0]) and decks[1][0] < len(decks[1]):
            # print("sub game")
            w = play_game([decks[0][1:decks[0][0]+1], decks[1][1:decks[1][0]+1]])
        if w == 0 or (w is None and decks[0][0] > decks[1][0]):
            # print(f"1 wins")
            decks[0].append(decks[0][0])
            decks[0].append(decks[1][0])
            decks[0].pop(0)
            decks[1].pop(0)
        elif w == 1 or (w is None and decks[1][0] > decks[0][0]):
            # print(f"2 wins")
            decks[1].append(decks[1][0])
            decks[1].append(decks[0][0])
            decks[0].pop(0)
            decks[1].pop(0)
        i += 1
    return 0 if decks[0] else 1

def p2(inp):
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
    play_game(decks)
    # print(f"ducks {decks}")
    score = 0
    winner = decks[0]
    if decks[1]: winner = decks[1]
    i = len(winner)
    for card in winner:
        score += card * i
        i -= 1
    # print(decks)
    return score



inp = get_input()
# print(p1(inp))
print(p2(inp))
