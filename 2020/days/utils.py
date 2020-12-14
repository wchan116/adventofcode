import sys


def get_input():
    if len(sys.argv) != 2:
        return [l.strip() for l in sys.stdin]
    else:
        with open(sys.argv[1]) as f:
            return [l.strip() for l in f.readlines()]
