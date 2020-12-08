#!/usr/bin/env ts-node-script

import get_input from '../utils/getline';

let input: string = get_input();

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

const p1 = (inp: string): number => {
    return getHousesVisited(inp).size;
}

const p2 = (inp: string): number => {
    let santa_path: string = "";
    let robot_path: string = "";

    for (let i = 0; i < inp.length; ++i) {
        if (i % 2 === 0) {
            santa_path += inp[i];
        }
        else {
            robot_path += inp[i];
        }
    }
    const shouses = getHousesVisited(santa_path);
    const rhouses = getHousesVisited(robot_path);
    const housesVisited = new Set([...shouses, ...rhouses]);

    return housesVisited.size;
}

console.log(p1(input));
console.log(p2(input));