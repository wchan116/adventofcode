#!/usr/bin/env ts-node-script

import get_input from '../utils/getline';

let input: string[] = get_input();

const goToFloor = (input: string, stopAt) => {
    let floor: number = 0;

    for (let i = 0; i < input.length; ++i) {
        if (input[i] === '(') {
            ++floor;
        }
        else if (input[i] === ')') {
            --floor;
        }
        
        if (floor === stopAt) {
            return i + 1;
        }
    }

    return floor;

}
const p1 = (inp: string[]): number => {
    return goToFloor(inp[0], null);
}

const p2 = (inp: string[]): number => {
    return goToFloor(inp[0], -1);
}

console.log(p1(input));
console.log(p2(input));