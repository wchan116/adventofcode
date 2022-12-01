#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun get_calories(input: List<String>): MutableList<Int> {
    var elves: MutableList<Int> = mutableListOf(0)
    input.forEach {
        if (it == "") {
            elves.add(0)
        } else {
            elves[elves.lastIndex] += it.toInt()
        }
    }
    return elves
}

fun p1(input: List<String>): Int {
    return get_calories(input).max()
}

fun p2(input: List<String>): Int {
    return get_calories(input).sorted().takeLast(3).sum()
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
