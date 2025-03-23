package com.rsk

fun main() {
    val nums = arrayOf(1)
    

    val ans = try {
        nums[1]
    } catch (t: Throwable) {
        0
    }
    println("The answer is $ans")
}

