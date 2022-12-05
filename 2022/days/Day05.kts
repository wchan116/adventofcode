#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun parse_input(input: List<String>): MutableMap<Int, ArrayDeque<Char>> {
    var stacks: MutableMap<Int, ArrayDeque<Char>> = mutableMapOf()
    input.forEach {
        var spaces = 0
        if (it.startsWith("move")) {
        } else if(it.startsWith(" 1")) {
        } else {
            it.forEach { char ->
                if (char == ' ') {
                    spaces++
                } else if (char == '[' || char == ']') {

                } else {
                    val pos = spaces / 4
                    if (stacks[pos].isNullOrEmpty()) {
                        stacks[pos] = ArrayDeque<Char>()
                    }
                    stacks[pos]!!.add(char)
                    spaces += 3
                }

            }
        }
    }
    return stacks
}
fun p1(input: List<String>): String {
    var stacks = parse_input(input)
    input.forEach {
        if (it.startsWith("move")) {
//            println(stacks.toSortedMap())
            val regex = "move (\\d+) from (\\d+) to (\\d+)".toRegex()
            val matches = regex.find(it)
            val (amount, from, to) = matches!!.groups.drop(1).map { it!!.value.toInt() }
            val removed = (1..amount).map { stacks[from-1]!!.removeFirst() }
            removed.forEach { stacks[to-1]!!.addFirst(it) }
        }
    }
    return stacks.toSortedMap().values.map { it.first() }.joinToString("")
}

fun p2(input: List<String>): String {
    var stacks = parse_input(input)
    input.forEach {
        if (it.startsWith("move")) {
            println(stacks.toSortedMap())
            val regex = "move (\\d+) from (\\d+) to (\\d+)".toRegex()
            val matches = regex.find(it)
            val (amount, from, to) = matches!!.groups.drop(1).map { it!!.value.toInt() }
            val removed = (1..amount).map { stacks[from-1]!!.removeFirst() }
            println(removed)
            removed.reversed().forEach { stacks[to-1]!!.addFirst(it) }
        }
        println(stacks.toSortedMap())
    }
    return stacks.toSortedMap().values.map { it.first() }.joinToString("")
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
