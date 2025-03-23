package com.rsk

fun main(args: Array<String>) {
    for (a in args) {
        print(a)
    }

    println()
    var value: Int = sum(23, 42)
    println(value)

    println()
    value = sum2(26, 47)
    println(value)

    doNothing()
}

fun sum(a: Int, b: Int): Int {
    return a + b
}

fun sum2(a: Int, b: Int) = a + b

fun doNothing() : Unit {
    println("Called doNothing")
}