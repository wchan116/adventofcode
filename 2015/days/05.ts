#!/usr/bin/env ts-node-script

import getline from '../utils/getline';

let input: string[] = getline();

const isNice = (inp: string[], pred): number => {
    let nice: number = 0;
    for (const str of inp) {
        if (pred(str)) {
            ++nice;
        }
    }
    return nice;
}

const p1 = (inp: string[]): number => {
    return isNice(inp, p1good);
}

const p1good = (str: string) => {
    return !containsBadSubstr(str) && countVowels(str) >= 3 && isCharConsecutive(str);
}

const containsBadSubstr = (str: string): boolean => {
    let substrs: string[] = ['ab', 'cd', 'pq', 'xy'];
    for (const substr of substrs) {
        if (str.includes(substr)) {
            return true;
        }
    }
    return false;
}

const countVowels = (str: string): number => {
    let vowels: number = 0;
    for (const char of str) {
        if (isVowel(char)) ++vowels;
    }

    return vowels;
}

const isCharConsecutive = (str: string): boolean => {
    let prev = str[0];
    for (let i = 1; i < str.length; ++i) {
        if (str[i] == prev) {
            return true;
        }
        prev = str[i];
    }
    return false;
}

const isVowel = (char): boolean => {
    return char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u';
}

const p2 = (inp: string[]): number => {
    return isNice(inp, p2good);
}

const p2good = (str: string): boolean => {
    return containsPair(str) && containsRptSepChar(str);
}

const containsPair = (str: string): boolean => {
    for (let i = 0; i < str.length; ++i) {
        let x = str[i];
        let y = str[i+1];
        for (let j = 0; j < str.length; ++j) {
            if (i == j || i + 1 == j || j + 1 == i || i + 1 == j + 1) continue;
            if (x == str[j] && y == str[j+1]) {
                return true;
            }
        }
    }

    return false;
}

const containsRptSepChar = (str: string): boolean => {
    for (let i = 0; i < str.length - 2; ++i) {
        if (str[i] == str[i + 2]) {
            return true;
        }
    }
    return false;
}

console.log(p1(input));
console.log(p2(input));