from utils import get_input

def find_loop_size(subject_number, key):
    sn = subject_number
    loop = 0
    while sn != key:
        sn = sn * subject_number
        sn = sn % 20201227

        loop += 1

    return loop

def transform(subject_number, loop):
    sn = subject_number

    for i in range(loop):
        sn = sn * subject_number
        sn = sn % 20201227
    return sn

def p1(inp):
    card_public_key = int(inp[0])
    door_public_key = int(inp[1])

    card_loop = find_loop_size(7, card_public_key)
    door_loop = find_loop_size(7, door_public_key)

    return transform(door_public_key, card_loop)


def p2(inp):
    pass


inp = get_input()
print(p1(inp))
print(p2(inp))
