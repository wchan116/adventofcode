#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun getValue(c: Char) = when {
    (('a'..'z').contains(c)) -> c.code - 96
    (('A'..'Z').contains(c)) -> (c.code - 65) + 27
    else -> 0
}

fun p1(input: List<String>): Int {
    var sum = 0
    input.forEach {
        val len = it.length
        val first = it.slice(0..(len/2)-1).toCharArray().toSet()
        val second = it.slice((len/2)..len-1).toCharArray().toSet()
        val same = first.intersect(second).first()
        sum += getValue(same)
    }
    return sum

}

fun p2(input: List<String>): Int {
    var sum = 0
    var intersect: Set<Char> = setOf()

    input.forEachIndexed { i, it ->
        if (i % 3 == 0) {
            intersect = it.toCharArray().toSet()
        }
        intersect = intersect.intersect(it.toCharArray().toSet())
        if (intersect.size == 1) {
            sum += getValue(intersect.first())
        }
    }

    return sum
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
