#!/usr/bin/env kscript

@file:Include("Utils.kts")

data class Node(
    val children: MutableSet<String>,
    val size: Int,
    val dir: Boolean
)

fun get_path(history: ArrayDeque<String>) = history.joinToString("/")

fun get_dir_size(directories: MutableMap<String, Node>, dir: String): Int {
    if (!directories[dir]!!.dir) {
        return directories[dir]!!.size
    }

    var total = 0
    directories[dir]!!.children.forEach {
        var size = get_dir_size(directories, "$dir/$it")
        total += size
    }
    return total
}

fun parse_input(input: List<String>): MutableMap<String, Node> {
    var directories: MutableMap<String, Node> = mutableMapOf()
    var history: ArrayDeque<String> = ArrayDeque()
    input.forEach {
        var command = it.replace("^\\$ ".toRegex(), "").split(" ")
        if (command[0] == "cd") {
            if (command[1] == "..") {
                history.removeLast()
            } else {
                history.add(command[1])
                if (!directories.containsKey(get_path(history))) {
                    directories.put(get_path(history), Node(mutableSetOf(), 0, true))
                }
            }
        } else if (command[0].toIntOrNull() != null) {
            val child = Node(mutableSetOf(), command[0].toInt(), false)
            val path = "${get_path(history)}/${command[1]}"
            directories[get_path(history)]!!.children.add(command[1])
            directories.put(path, child)
        } else if (command[0] == "dir") {
            val child = Node(mutableSetOf(), 0, true)
            val path = "${get_path(history)}/${command[1]}"
            directories[get_path(history)]!!.children.add(command[1])
            directories.put(path, child)
        }
    }
    return directories
}

fun p1(input: List<String>): Int {
    val directories = parse_input(input)
    return directories.filter { it.value.dir && it.key != "/" }.keys.fold(0) { total, key ->
        var size = get_dir_size(directories, key)
        if (size <= 100_000) total + size else total
    }
}

fun p2(input: List<String>): Int {
    val goal = 30000000
    var total = 70000000
    val directories = parse_input(input)

    var root = get_dir_size(directories, "/")
    var unused = total - root
    return directories.filter { it.value.dir }.keys.minOf { key ->
        var size = get_dir_size(directories, key)
        if (unused + size >= goal) {
            size
        } else {
            Int.MAX_VALUE
        }
    }
}

val inp = Utils.readFromFileIntoList(args[0])!!
println(p1(inp))
println(p2(inp))
