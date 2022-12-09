#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun getDistance(x: Pair<Int, Int>, y: Pair<Int, Int>) = maxOf(Math.abs(x.first - y.first), Math.abs(x.second - y.second))

fun findDir(x: Pair<Int, Int>, y: Pair<Int, Int>): String {
    return when {
        x.first == y.first && x.second > y.second -> "U"
        x.first == y.first && x.second < y.second -> "D"
        x.second == y.second && x.first > y.first -> "R"
        x.second == y.second && x.first < y.first -> "L"
        x.first > y.first && x.second > y.second -> "NE"
        x.first < y.first && x.second > y.second -> "NW"
        x.first > y.first && x.second < y.second -> "SE"
        x.first < y.first && x.second < y.second -> "SW"
        else -> ""
    }
}

fun move(x: Pair<Int, Int>, dir: String): Pair<Int, Int> {
    return when (dir) {
        "L" -> Pair(x.first - 1, x.second)
        "R" -> Pair(x.first + 1, x.second)
        "U" -> Pair(x.first, x.second + 1)
        "D" -> Pair(x.first, x.second - 1)
        "NE" -> Pair(x.first + 1, x.second + 1)
        "NW" -> Pair(x.first - 1, x.second + 1)
        "SE" -> Pair(x.first + 1, x.second - 1)
        "SW" -> Pair(x.first - 1, x.second - 1)
        else -> Pair(x.first, x.second)
    }
}

fun track_rope(input: List<String>, ropeSize: Int): Int {
    var visited: MutableSet<Pair<Int, Int>> = mutableSetOf(Pair(0, 0))
    var rope: MutableList<Pair<Int, Int>> = mutableListOf()

    (1..ropeSize).forEach { rope.add(Pair(0, 0)) }

    input.forEach {
        val (dir, steps) = it.split(" ")
        for (i in 1..steps.toInt()) {
            rope[0] = move(rope[0], dir)
            for (i in 1..rope.size-1) {
                if (getDistance(rope[i-1], rope[i]) > 1) {
                    val direction = findDir(rope[i-1], rope[i])
                    rope[i] = move(rope[i], direction)
                    visited.add(rope[ropeSize-1])
                }
            }
        }
    }

    return visited.size
}

fun p1(input: List<String>) = track_rope(input, 2)

fun p2(input: List<String>) = track_rope(input, 10)

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
