#!/usr/bin/env kscript -S JAVA_OPTS="-Xmx32g"

@file:Include("Utils.kts")

import java.util.Queue
import java.util.LinkedList

val directions = listOf(
    Pair(0, 1),
    Pair(0, -1),
    Pair(1, 0),
    Pair(-1, 0),
)

fun bfs(grid: List<List<Char>>, start: Pair<Int, Int>, elevation: (Char, Char) -> Boolean): MutableMap<Pair<Int, Int>, Int> {
    var visited: MutableSet<Pair<Int, Int>> = mutableSetOf()
    var queue: Queue<Pair<Int, Int>> = LinkedList<Pair<Int, Int>>()
    var distance: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()
    queue.offer(start)
    distance.put(start, 0)

    while (queue.isNotEmpty()) {
        var node = queue.poll()

        visited.add(node)
        directions.forEach {
            val neighbour = Pair(node.first + it.first, node.second + it.second)
            if (neighbour.first in (0..grid.size-1) && neighbour.second in (0..grid[0].size-1)) {
                var nodeElev = grid[node.first][node.second]
                var neighbourElev = grid[neighbour.first][neighbour.second]
                if (elevation(neighbourElev, nodeElev)) {
                    distance[neighbour] = minOf(distance[node]!! + 1, distance.getOrDefault(neighbour, Int.MAX_VALUE))
                    if (!visited.contains(neighbour) && !queue.contains(neighbour)) {
                        queue.offer(neighbour)
                    }
                }
            }
        }
    }

    return distance
}

fun processInput(input: List<String>): Triple<List<List<Char>>, Pair<Int, Int>, Pair<Int, Int>> {
    var grid: MutableList<MutableList<Char>> = mutableListOf()
    var end: Pair<Int, Int> = Pair(0, 0)
    var start = Pair(0, 0)

    input.forEachIndexed { rowIndex, row ->
        grid.add(mutableListOf())
        row.forEachIndexed { colIndex, col ->
            var cell = col
            if (col == 'E') {
                end = Pair(rowIndex, colIndex)
                cell = 'z'
            } else if (col == 'S') {
                start = Pair(rowIndex, colIndex)
                cell = 'a'
            }
            grid.last().add(cell)
        }
    }

    return Triple(grid, start, end)
}

fun p1(input: List<String>): Int{
    val (grid, start, end) = processInput(input)

    val distance = bfs(grid, start, { x, y -> x - y <= 1})
    return distance[end]!!
}

fun p2(input: List<String>): Int {
    val (grid, start, end) = processInput(input)
    val distance = bfs(grid, end, { x, y -> y - x <= 1})
    return distance.filter { grid[it.key.first][it.key.second] == 'a' }.minOf {
        it.value
    }
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
