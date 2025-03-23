package com.rsk

fun main() {
    val name = "Kevin"
    val age = 21

    val message = "Name is ${name.lowercase()} and age is $age"

    println("Name is $name and age is $age")
    println("Name is ${name.uppercase()} and age is $age")
    println(message)
}