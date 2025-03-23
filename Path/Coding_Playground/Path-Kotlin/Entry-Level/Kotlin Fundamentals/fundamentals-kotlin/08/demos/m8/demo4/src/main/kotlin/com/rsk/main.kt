package com.rsk

class Invoice {

    companion object Logger {
        fun debug(message: String) {
            println("($this) ${message}")
        }
    }

    fun calculate() {
        debug("calculating invoice")
    }
}

fun main() {
    val invoice = Invoice()

    invoice.calculate()
    val invoice2 = Invoice()

    invoice2.calculate()

    Invoice.debug("Like a static")

//    Invoice.Logger.debug("called from main")
}