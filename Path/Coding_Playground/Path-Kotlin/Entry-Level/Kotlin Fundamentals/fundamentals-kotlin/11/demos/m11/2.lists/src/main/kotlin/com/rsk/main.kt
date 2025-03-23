package com.rsk

data class Person(val name: String)

fun main() {
    val people = mutableMapOf<Int, Person>(1 to Person("Kevin"), 2 to Person("Teresa"), 3 to Person("Harry"))

    for ((index, person) in people) {
        println("$index is $person")
    }
}

fun lists() {
    val numbers = mutableListOf(1, 2, 3, 4)

    for (num in numbers) {
        println(num)
    }

    val n = numbers[0]

    println(n)

    numbers[0] = 5

    println(numbers[0])

    numbers.add(23)

    for (num in numbers) {
        println(num)
    }
}