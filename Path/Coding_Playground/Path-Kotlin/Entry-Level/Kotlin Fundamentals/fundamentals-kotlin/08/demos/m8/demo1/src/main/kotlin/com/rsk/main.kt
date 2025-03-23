package com.rsk

fun main() {
    val simple = object {
        val name = "Kevin"

        fun printValue() {
            println(name)
        }
    }

    println(simple.name)
    simple.printValue()
}

