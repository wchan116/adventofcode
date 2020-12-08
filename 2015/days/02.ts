#!/usr/bin/env ts-node-script

import get_input from '../utils/getline';

let input: string = get_input();
let sizes: Array<Array<number>> = [];

const regex = /(\d+)x(\d+)x(\d+)/;
for (const line of input) {
    const lm = line.match(regex);
    if (lm) {
        sizes.push(lm.slice(1).map(elem => parseInt(elem)));
    }
}

const p1 = (sizes: Array<Array<number>>): number => {
    let total: number = 0;

    for (const size of sizes) {
        let [l, w, h] = size;
        total += (2 * l * w) + (2 * w * h) + (2 * h * l) + Math.min(w * l, w * h, h * l);
    }

    return total;
};

const p2 = (sizes: Array<Array<number>>): number => {
    let total: number = 0;
    for (const size of sizes) {
        let [l, w, h] = size;
        total += (l * w * h) + Math.min((l + w) * 2, (w + h) * 2, (h + l) * 2);
    }

    return total;
};

console.log(p1(sizes));
console.log(p2(sizes));