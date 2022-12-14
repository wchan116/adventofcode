#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun process_input(input: List<String>): MutableSet<Pair<Int, Int>> {
    val rocks: MutableSet<Pair<Int, Int>> = mutableSetOf()

    var max_y = 0
    input.forEach {
        var line = it.split("->").map { it.strip() }
        var prev: Pair<Int, Int>? = null
        for (l in line) {
            var (x, y) = l.split(",").map { it.toInt() }
            max_y = maxOf(max_y, y)
            if (prev != null) {
                if (prev.first == x) {
                    if (prev.second < y) {
                        for (i in prev!!.second..y) {
                            rocks.add(Pair(x, i))
                        }
                    } else if (prev.second > y) {
                        for (i in y..prev!!.second) {
                            rocks.add(Pair(x, i))
                        }
                    }
                } else if (prev.second == y) {
                    if (prev.first < x) {
                        for (i in prev!!.first..x) {
                            rocks.add(Pair(i, y))
                        }
                    } else if (prev.first > x) {
                        for (i in x..prev!!.first) {
                            rocks.add(Pair(i, y))
                        }
                    }

                }

            }
            prev = Pair(x, y)

        }
    }
    return rocks
}

fun p1(input: List<String>): Int {
    var rocks = process_input(input)

//    println(rocks)
    var sand = Pair(500, 0)
    var rest = 0
    var inAbyss = false
    val max_y = rocks.maxOf { it.second }

    while (!inAbyss) {
        var atRest = false
        sand = Pair(500, 0)
        while (!atRest) {
            var next = sand.copy(sand.first, sand.second + 1)
            if (rocks.contains(next)) {
                next = sand.copy(sand.first - 1, sand.second + 1)
                if (rocks.contains(next)) {
                    next = sand.copy(sand.first + 1, sand.second + 1)
                    if (rocks.contains(next)) {
                        atRest = true
                        rest++
                    }
                }
            }
//            println(next)
//            println(rest)
            if (sand.second >= max_y) {
                inAbyss = true
                break
            }
            if (atRest) {
                rocks.add(sand)
            }
            sand = next
        }
    }
//    println(sand)
//    println(rest)
    return rest
}

fun p2(input: List<String>) {
    var rocks = process_input(input)

//    println(rocks)
    var sand = Pair(500, 0)
    var rest = 0
    var inAbyss = false
    val max_y = rocks.maxOf { it.second } + 2

    while (!inAbyss) {
        var atRest = false
        sand = Pair(500, 0)
        while (!atRest) {
            var next = sand.copy(sand.first, sand.second + 1)
            if (rocks.contains(next) || next.second >= max_y) {
                next = sand.copy(sand.first - 1, sand.second + 1)
                if (rocks.contains(next) || next.second >= max_y) {
                    next = sand.copy(sand.first + 1, sand.second + 1)
                    if (rocks.contains(next) || next.second >= max_y) {
                        atRest = true
                        rest++
                    }
                }
            }
//            println(next)
//            println(rest)
            if (rocks.contains(Pair(500, 0))) {
                inAbyss = true
                break
            }
            if (atRest) {
                rocks.add(sand)
            }
            sand = next
        }
    }
//    println(sand)
    println(rest - 1)

}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
