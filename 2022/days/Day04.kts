#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun getSortedIntervals(input: List<String>) = input.map {
    it.split(",").map {
        val pair = it.split("-")
        Pair<Int, Int>(pair[0].toInt(), pair[1].toInt())
    }.sortedWith(compareBy<Pair<Int, Int>>({ it.first }).thenByDescending({ it.second }))
}

fun p1(input: List<String>): Int {
    return getSortedIntervals(input).count {
        it[1].first >= it[0].first && it[1].second <= it[0].second
    }
}

fun p2(input: List<String>): Int {
    return getSortedIntervals(input).count {
       it[1].first <= it[0].second
    }
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
