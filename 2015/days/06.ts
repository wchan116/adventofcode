#!/usr/bin/env ts-node-script

import getline from '../utils/getline';

let input: string = getline();

const transformLights = (inp: string, onFunc, offFunc, toggleFunc): number[][] => {
    const regex = /(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)/;
    let lights: number[][] = new Array(1000).fill(0).map(() => new Array(1000).fill(0));
    for (const line of inp) {
        const lm = line.match(regex);
        if (lm) {
            let op = lm[1];
            let [start_x, start_y, end_x, end_y] = lm.slice(2).map(elem => parseInt(elem));
            if (op === 'turn on') {
                for (let i = start_x; i < end_x + 1; ++i) {
                    for (let j = start_y; j < end_y + 1; ++j) {
                        lights[i][j] = onFunc(lights[i][j]);
                    }
                }
            }
            else if (op === 'turn off') {
                for (let i = start_x; i < end_x + 1; ++i) {
                    for (let j = start_y; j < end_y + 1; ++j) {
                        lights[i][j] = offFunc(lights[i][j]);
                    }
                }
            }
            else if (op === 'toggle') {
                for (let i = start_x; i < end_x + 1; ++i) {
                    for (let j = start_y; j < end_y + 1; ++j) {
                        lights[i][j] = toggleFunc(lights[i][j]);
                    }
                }
            }
        }
    }
    
    return lights;
}

const p1 = (inp: string): number => {
    let lights: number[][] = transformLights(inp, (light) => 1, (light) => 0, (light) => light ^ 1 );
    return countBrightness(lights);
}

const p2 = (inp: string): number => {
    let lights: number[][] = transformLights(inp, 
                                            (light) => light + 1, 
                                            (light) => (light - 1 < 0) ? 0 : light - 1,
                                            (light) => light + 2 );
    return countBrightness(lights);
}

const countBrightness = (lights: number[][]): number => {
    let nlights: number = 0;
    for (let i = 0; i < 1000; ++i) {
        for (let j = 0; j < 1000; ++j) {
            nlights += lights[i][j];
        }
    }
    return nlights;
}

console.log(p1(input));
console.log(p2(input));