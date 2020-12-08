#!/usr/bin/env ts-node-script

import get_input from '../utils/getline';

let input: string = get_input();

const p1 = (inp: string): number => {
    let floor: number = 0;

    for (const action of inp) {
        if (action === '(') {
            ++floor;
        }
        else if (action === ')') {
            --floor;
        }
    }

    return floor;
}

const p2 = (inp: string): number => {
    let floor: number = 0;

    for (let i = 0; i < inp.length; ++i) {
        if (inp[i] === '(') {
            ++floor;
        }
        else if (inp[i] === ')') {
            --floor;
        }
        
        if (floor === -1) {
            return i + 1;
        }
    }
    return -1;
}

console.log(p1(input));
console.log(p2(input));