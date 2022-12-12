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

fun bfs(grid: List<List<Char>>, start: Pair<Int, Int>, end: Pair<Int, Int>): Int {
    var visited: MutableSet<Pair<Int, Int>> = mutableSetOf()
    var queue: Queue<Pair<Int, Int>> = LinkedList<Pair<Int, Int>>()
    var distance: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()
    queue.offer(start)
    distance.put(start, 0)

    while (queue.isNotEmpty()) {
        var node = queue.poll()

        if (node == end) {
            return distance[node]!!
        }

        visited.add(node)
        directions.forEach {
            val neighbour = Pair(node.first + it.first, node.second + it.second)
            if (neighbour.first in (0..grid.size-1) && neighbour.second in (0..grid[0].size-1)) {
                var nodeElev = grid[node.first][node.second]
                var neighbourElev = grid[neighbour.first][neighbour.second]
                if (neighbourElev - nodeElev <= 1) {
                    distance[neighbour] = minOf(distance[node]!! + 1, distance.getOrDefault(neighbour, Int.MAX_VALUE))
                    if (!visited.contains(neighbour) && !queue.contains(neighbour)) {
                        queue.offer(neighbour)
                    }
                }
            }
        }
    }

    return Int.MAX_VALUE
}

fun p1(input: List<String>): Int{
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

    return bfs(grid, start, end)
}

fun p2(input: List<String>): Int {
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
    var steps = Int.MAX_VALUE

//    grid.forEachIndexed { rowIndex, row ->
//        row.forEachIndexed { colIndex, col ->
//            if (col == 'a') {
//                steps = minOf(steps, bfs(grid, Pair(rowIndex, colIndex), end))
//
//            }
//        }
//    }
    var visited: MutableSet<Pair<Int, Int>> = mutableSetOf()
    var queue: Queue<Pair<Int, Int>> = LinkedList<Pair<Int, Int>>()
    var distance: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()
    var eleDistance: MutableMap<Char, Int> = mutableMapOf()
    queue.offer(end)
    distance.put(end, 0)
    eleDistance.put(grid[end.first][end.second], 0)

    while (queue.isNotEmpty()) {
        var node = queue.poll()

        visited.add(node)
        directions.forEach {
            val neighbour = Pair(node.first + it.first, node.second + it.second)
            if (neighbour.first in (0..grid.size-1) && neighbour.second in (0..grid[0].size-1)) {
                var nodeElev = grid[node.first][node.second]
                var neighbourElev = grid[neighbour.first][neighbour.second]
                if (nodeElev - neighbourElev <= 1) {
                    distance[neighbour] = minOf(distance[node]!! + 1, distance.getOrDefault(neighbour, Int.MAX_VALUE))
                    eleDistance[neighbourElev] = minOf(eleDistance[nodeElev]!! + 1, eleDistance.getOrDefault(neighbourElev, Int.MAX_VALUE))
                    if (!visited.contains(neighbour) && !queue.contains(neighbour)) {
                        queue.offer(neighbour)
                    }
                }
            }
        }
    }
    distance.forEach {
        if (grid[it.key.first][it.key.second] == 'a') {
            steps = minOf(steps, it.value)

        }

    }
    return steps

}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
