#!/usr/bin/env ts-node-script

import get_input from '../utils/getline';

let input: string[] = get_input();

const getHousesVisited = (inp: string): Set<unknown> => {
    let pos = [0, 0];
    let seen = new Set();
    seen.add(JSON.stringify(pos.slice()));

    for (const dir of inp) {
        if (dir === '^') {
            pos[1]++;
        }
        else if (dir === 'v') {
            pos[1]--;
        }
        else if (dir === '>') {
            pos[0]++;
        }
        else if (dir === '<') {
            pos[0]--;
        }
        seen.add(JSON.stringify(pos.slice()));
    }

    return seen;
}

const p1 = (inp: string[]): number => {
    return getHousesVisited(inp[0]).size;
}

const p2 = (inp: string[]): number => {
    const input = inp[0]
    let santa_path: string = "";
    let robot_path: string = "";

    for (let i = 0; i < input.length; ++i) {
        if (i % 2 === 0) {
            santa_path += input[i];
        }
        else {
            robot_path += input[i];
        }
    }
    const shouses = getHousesVisited(santa_path);
    const rhouses = getHousesVisited(robot_path);
    const housesVisited = new Set([...shouses, ...rhouses]);

    return housesVisited.size;
}

console.log(p1(input));
console.log(p2(input));