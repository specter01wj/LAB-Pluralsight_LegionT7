package com.rsk

object Logger {
    fun debug(message: String) {
        println("** debug: $this $message")
    }

    fun info(message: String) {
        println("** info: $message")
    }

}

class Person {
    fun doWork() {
        Logger.debug("some message")
    }
}

fun main() {
    val kevin = Person()

    kevin.doWork()

    val terry = Person()

    terry.doWork()
}