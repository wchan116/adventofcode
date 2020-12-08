#!/usr/bin/env ts-node-script

const fs = require('fs');
const readline = require('readline');

const get_input = (): string => {
    if (process.argv.length != 3) {
        return fs.readFileSync(0, 'utf8');
    }
    else {
        return fs.readFileSync(process.argv[2], 'utf8');
    }
}

export default get_input;