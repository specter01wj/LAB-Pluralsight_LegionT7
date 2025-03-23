package com.rsk

fun main() {

    val arr = intArrayOf(1, 2, 3, 4, 5)
    val arr1 = arrayOf("Kevin", "Jones")

    println("Name is ${arr1[0]} ${arr1[1]}")

    arr1[1] = "Smith"
    println("Name is ${arr1[0]} ${arr1[1]}")
}