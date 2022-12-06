#!/usr/bin/env kscript

@file:Include("Utils.kts")

fun is_window_unique(window: String): Boolean {
    return window.length == window.toSet().size
}

fun get_first_unique_window_index(input: String, window_size: Int): Int {
    var left = 0
    var right = window_size - 1
    while (right < input.length) {
        var window = input.slice(left..right)
        if (is_window_unique(window)) {
            return right + 1
        }
        ++left
        ++right
    }
    return 0
}

fun p1(input: String) = get_first_unique_window_index(input, 4)

fun p2(input: String) = get_first_unique_window_index(input, 14)

val inp = Utils.readFromFile(args[0])!!
println(p1(inp))
println(p2(inp))
