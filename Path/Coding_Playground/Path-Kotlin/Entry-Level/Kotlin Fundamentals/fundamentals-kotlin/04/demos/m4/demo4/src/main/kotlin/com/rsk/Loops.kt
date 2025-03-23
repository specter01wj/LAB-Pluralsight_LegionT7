package com.rsk

fun main() {
    var outer = 5
    var inner = 5

    outer@ while(outer > 1) {
        outer--
        while(inner > 1) {
            inner--

            if (outer == 3) break@outer
            println("Values are $outer and $inner")
        }
        inner = 5
    }

//    var count = 5
//
//    while (count > 1) {
//        println("Always printed $count")
//        count--
//
//        if(count > 3) continue
//        println("Sometimes printed $count")
//
//    }

//    println()
//    count = 1
//    do {
//        println(count)
//        count--
//
//    } while (count > 1)
}