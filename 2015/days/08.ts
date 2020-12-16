#!/usr/bin/env ts-node-script

import getline from '../utils/getline';

let input: string[] = getline();

const p1 = (inp: string[]): number => {
    let total_chars: number = 0;
    let total_mem_chars: number = 0;
    for (let i of inp) {
        total_chars += i.length;
        i = i.slice(1, i.length - 1).replace(/\\\\/g, '\\').replace(/\\\"/g, '"').replace(/\\x[a-f0-9]{2}/g, '1');
        total_mem_chars += i.length;
    }
    return total_chars - total_mem_chars;
}

const p2 = (inp: string[]): number => {
    let total_chars: number = 0;
    let total_mem_chars: number = 0;
    for (let i of inp) {
        total_chars += i.length;
        i = i.slice(1, i.length - 1);
        let n: number = 6 + i.length;
        for (let c of i) {
            if (c === '"' || c === '\\') {
                ++n;
            }
        }
        total_mem_chars += n;
    }
    return total_mem_chars - total_chars;
}

console.log(p1(input));
console.log(p2(input));