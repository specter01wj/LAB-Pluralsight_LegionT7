package com.rsk


// override toString
data class Person(val name: String, val age: Int)

fun main() {

    val sam = Person("Sam",31)
    val samuel = sam.copy(age = 32)


    println("$sam, has hashCode ${sam.hashCode()}")
    println("$samuel, has hashCode ${samuel.hashCode()}")

    val (n, a) = samuel
    println("Samuel has the ${n} and the age ${a}")

}