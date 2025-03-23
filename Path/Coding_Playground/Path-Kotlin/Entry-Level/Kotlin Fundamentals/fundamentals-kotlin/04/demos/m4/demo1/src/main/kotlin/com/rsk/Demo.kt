package com.rsk

fun main() {
    val a = 23
    val b = 10


//    if(a < b)
//        min = a
//    else
//        min = b

//    val min = if (a < b) a else b
    val min = if (a < b) {
        println("about to return a")
        a
    }
    else {
        println("about to return b")
        b
    }

    println("min is $min")
}