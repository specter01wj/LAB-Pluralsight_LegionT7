package com.rsk

fun main() {
    val numbers = listOf(10, 23, 3, 42, 51, 123, 6, 8, 99)

    val seq = numbers.asSequence()

    val newNumbers = numbers
        .asSequence()
        .filter {
            println("filter: $it")
            it > 9
        }
        .map {
            println("map: $it")
            it * 3
        }
        .take(3)
        .joinToString(",")

    println(newNumbers)
}



