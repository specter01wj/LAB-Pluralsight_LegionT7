package com.rsk

fun main() {
    val nums = arrayOf(5)

    try {
        val num = nums[1]
    } catch (t: Throwable) {
        println(t.message)
    }
//    println("value is $num")
}