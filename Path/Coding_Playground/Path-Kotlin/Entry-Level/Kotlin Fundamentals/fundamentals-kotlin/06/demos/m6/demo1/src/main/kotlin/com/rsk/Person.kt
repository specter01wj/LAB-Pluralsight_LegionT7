package com.rsk


// override toString
data class Person(val name: String, val age: Int)

fun main() {

    val sam = Person("Sam", 31)
    val samuel = Person("Sam", 31)

    println("$sam, has hashCode ${sam.hashCode()}")
    println("$samuel, has hashCode ${samuel.hashCode()}")

    if(sam.equals(samuel)) {
        println("these are the same")
    }

    if(sam === samuel) {
        println("these are the same")
    } else {
        println("these are not the same")
    }

}