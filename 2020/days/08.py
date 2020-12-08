import re
from utils import get_input

class Console:
    def __init__(self):
        self.acc = 0
        self.pc = 0

    def exec(self, instructions):
        """
        Return false if we detect a loop
        """
        self.acc = 0
        self.pc = 0

        n = len(instructions)
        seen = set()
        while self.pc < n:
            if self.pc in seen:
                return False
            seen.add(self.pc)
            im = re.match(r'(nop|acc|jmp) (\+|\-)(\d+)', instructions[self.pc])
            if im:
                op, sign, arg = im.groups(0)
                arg = int(arg)
                if sign == '-': arg *= -1
                
                if op == 'acc':
                    self.acc += arg
                elif op == 'jmp':
                    self.pc += arg
                    continue
                self.pc += 1
        return True
    
def p1(inp):
    console = Console()
    console.exec(inp)
    return console.acc

def p2(inp):
    console = Console()
    n = len(inp)
    for i in range(n):
        instructions = inp.copy()
        if inp[i].startswith('nop'):
            instructions[i] = instructions[i].replace('nop', 'jmp')
        elif inp[i].startswith('jmp'):
            instructions[i] = instructions[i].replace('jmp', 'nop')
        if console.exec(instructions):
            return console.acc
    return -1

inp = get_input()
print(p1(inp))
print(p2(inp))