package com.rsk

fun main() {
    try {
        throwException()
    } catch (e: Throwable) {
        println(e.message)
    } finally {
        println("Inside finally")
    }
}

fun throwException() {
    throw Exception("Some exception")
}