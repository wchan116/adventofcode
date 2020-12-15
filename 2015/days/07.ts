#!/usr/bin/env ts-node-script

import getline from '../utils/getline';

let input: string[] = getline();

const parseInstruction = (wires: Map<string, any>, wire: string, instruction: string): number => {
    if (instruction.toString().match(/^\d+$/)) {
        return wires.get(wire);
    }
    else {
        let lm: any;
        let res: number;

        if (lm = instruction.match(/^(\d+|\w+)$/)) {
            const val = lm[1];

            res = isNaN(parseInt(val)) ? parseInstruction(wires, val, wires.get(val)) : parseInstruction(wires, wire, val);

        }
        else if (lm = instruction.match(/^(\w+|\d+) AND (\w+|\d+)$/)) {
            let [val1, val2] = lm.slice(1);

            val1 = isNaN(parseInt(val1)) ? parseInstruction(wires, val1, wires.get(val1)) : parseInt(val1);
            val2 = isNaN(parseInt(val2)) ? parseInstruction(wires, val2, wires.get(val2)) : parseInt(val2);

            res = val1 & val2;
        }
        else if (lm = instruction.match(/^(\w+) OR (\w+)$/)) {
            let [val1, val2] = lm.slice(1);

            val1 = isNaN(parseInt(val1)) ? parseInstruction(wires, val1, wires.get(val1)) : parseInt(val1);
            val2 = isNaN(parseInt(val2)) ? parseInstruction(wires, val2, wires.get(val2)) : parseInt(val2);

            res = val1 | val2;
        }
        else if (lm = instruction.match(/^(\w+) LSHIFT (\d+)$/)) {
            let [wire1, num] = lm.slice(1);
            num = parseInt(num);

            wire1 = parseInstruction(wires, wire1, wires.get(wire1));
            res = wire1 << num;
        }
        else if (lm = instruction.match(/^(\w+) RSHIFT (\d+)$/)) {
            let [wire1, num] = lm.slice(1);
            num = parseInt(num);

            wire1 = parseInstruction(wires, wire1, wires.get(wire1));
            res = wire1 >> num;
        }
        else if (lm = instruction.match(/^NOT (\w+)$/)) {
            let wire1 = lm[1];

            wire1 = parseInstruction(wires, wire1, wires.get(wire1));
            res = 65536 + ~wire1;
        }

        wires.set(wire, res);
        return res;
    }
};

const p1 = (inp: string[]): number => {
    let wires: Map<string, any> = new Map();

    for (const line of inp) {
        let lm;
        if (lm = line.match(/^(.*) -> (\w+)$/)) {
            wires.set(lm[2], lm[1]);
        }
    }

    parseInstruction(wires, 'a', wires.get('a'));
    return wires.get('a');
};

const p2 = (inp: string[]): number => {
    const a: number = p1(inp);
    let wires: Map<string, any> = new Map();

    for (const line of inp) {
        let lm;
        if (lm = line.match(/^(.*) -> (\w+)$/)) {
            wires.set(lm[2], lm[1]);
        }
    }

    wires.set('b', a);
    parseInstruction(wires, 'a', wires.get('a'));
    return wires.get('a');
};

console.log(p1(input));
console.log(p2(input));