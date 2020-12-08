#!/usr/bin/env ts-node-script

const fs = require('fs');
const readline = require('readline');

const get_input = (): string => {
    let inp;
    if (process.argv.length != 3) {
        inp = fs.readFileSync(0, 'utf8');
    }
    else {
        inp = fs.readFileSync(process.argv[2], 'utf8');
    }

    return inp.split(/\r?\n/).filter(line => line !== '').map(line => line.trim());
}

export default get_input;