#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun p1(input: List<String>): Int {
    var opp = mapOf("A" to 1, "B" to 2, "C" to 3)
    var you = mapOf("X" to 1, "Y" to 2, "Z" to 3)
    var winning = mapOf("A" to "Y", "B" to "Z", "C" to "X")
    var score = 0

    input.forEach {
        var (o_choice, y_choice) = it.split(' ')
        score += you[y_choice]!!
        if (winning[o_choice] == y_choice) {
            score += 6
        } else if (you[y_choice]!! == opp[o_choice]!!) {
            score += 3
        }
    }

    return score
}

fun p2(input: List<String>): Int {
    var opp = mapOf("A" to 1, "B" to 2, "C" to 3)
    var you = mapOf("X" to 1, "Y" to 2, "Z" to 3)
    var wld = mapOf("X" to 0, "Y" to 3, "Z" to 6)
    var winning = mapOf("A" to "Y", "B" to "Z", "C" to "X")
    var losing = mapOf("A" to "Z", "B" to "X", "C" to "Y")
    var score = 0

    input.forEach {
        var (o_choice, y_choice) = it.split(' ')
        score += wld[y_choice]!!
        if (y_choice == "X") {
            // lose
            score += you[losing[o_choice]!!]!!
        } else if (y_choice == "Y") {
            // draw
            score += opp[o_choice]!!
        } else if (y_choice == "Z") {
            //win
            score += you[winning[o_choice]!!]!!
        }
    }

    return score
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
