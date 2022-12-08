#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun p1(input: List<String>): Int {
    var visible = 0
    var grid = input.map { it.split("").filter { it != ""}.map { it.toInt() } }
    visible += (grid.size * 2 + (grid.size - 2) * 2)

    for (i in 1..grid.size-2) {
        for (j in 1..grid[0].size-2) {
            var v = false
            var left = true
            for (k in j-1 downTo 0) {
                left = left && grid[i][j] > grid[i][k]
            }
//            println("down")
            var right = true
            for (k in j+1..grid[0].size-1) {
                right = right && grid[i][j] > grid[i][k]
            }
            var up = true
            for (k in i-1 downTo 0) {
                up = up && grid[i][j] > grid[k][j]
            }
            var down = true
            for (k in i+1..grid.size-1) {
                down = down && grid[i][j] > grid[k][j]
            }

            if (up || down || left || right) {
                visible += 1
            }
        }
    }

    return visible
}

fun p2(input: List<String>): Int {
    var best_scenic = 0
    var grid = input.map { it.split("").filter { it != ""}.map { it.toInt() } }

    for (i in 0..grid.size-1) {
        for (j in 0..grid[0].size-1) {
            var left = 0
            for (k in j-1 downTo 0) {
                ++left
                if (grid[i][j] <= grid[i][k]) {
                    break
                }
            }
            var right = 0
            for (k in j+1..grid[0].size-1) {
                ++right
                if (grid[i][j] <= grid[i][k]) {
                    break
                }
            }
            var up = 0
            for (k in i-1 downTo 0) {
                ++up
                if (grid[i][j] <= grid[k][j]) {
                    break
                }
            }
            var down = 0
            for (k in i+1..grid.size-1) {
                ++down
                if (grid[i][j] <= grid[k][j]) {
                    break
                }
            }

            val score = up * down * left * right
            best_scenic = maxOf(best_scenic, score)
        }
    }

    return best_scenic
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
