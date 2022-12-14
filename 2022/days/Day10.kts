#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun p1(input: List<String>): Int {
    var cycles = 0
    var x = 1
    var signal = 0
    var history = mutableListOf<Int>()

    input.forEach {
        if (it.startsWith("noop")) {
            history.add(x)
            ++cycles
        } else {
            var (op, n) = it.split(" ")
            history.add(x)
            history.add(x)
            x += n.toInt()
            cycles += 2
        }
    }
    history.add(x)
    listOf(20, 60, 100, 140, 180, 220).forEach {
        signal += (it * history[it-1])
    }

    return signal
}

fun p2(input: List<String>) {
    var cycles = 0
    var x = 1
    var history = mutableListOf<Int>()

    input.forEach {
        if (it.startsWith("noop")) {
            history.add(x)
            ++cycles
        } else {
            var (op, n) = it.split(" ")
            history.add(x)
            history.add(x)
            x += n.toInt()
            cycles += 2
        }
    }
    history.add(x)

    var line = ""
    for (i in 0..history.size-1) {
        if (i % 40 == 0) {
            println(line)
            line = ""
        }
        if (listOf(history[i], history[i]-1, history[i]+1).contains(i % 40)) {
            line += "#"
        } else {
            line += "."
        }

    }
//    println(line)

}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
