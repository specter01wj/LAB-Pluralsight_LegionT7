package com.rsk

fun main() {
//    fibonacci(8, ::println)

    var total = 0

    fibonacci(8) {total += it}

    println(total)
}

fun fibonacci(limit: Int, action: (Int) -> Unit) {
    // 1, 1, 2, 3, 5, 8, 13, 21
    var prev = 0
    var prevprev = 0
    var current = 1

    for (i: Int in 1..limit) {
        action(current)

        var temp = current
        prevprev = prev
        prev = temp
        current = prev + prevprev
    }
}
