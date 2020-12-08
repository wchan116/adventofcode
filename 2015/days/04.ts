#!/usr/bin/env ts-node-script

const md5 = require('md5');
import get_input from '../utils/getline';

let input: string = get_input();

const findHashStartingWith = (inp: string, num: string): number  => {
    let i: number = 0;
    let hash: string = inp + i;

    while (!md5(hash).startsWith(num)) {
        ++i;
        hash = inp + i;
    }

    return i;
}

const p1 = (inp: string): number => {
    return findHashStartingWith(inp, '00000');
}

const p2 = (inp: string): number => {
    return findHashStartingWith(inp, '000000');
}

console.log(p1(input));
console.log(p2(input));