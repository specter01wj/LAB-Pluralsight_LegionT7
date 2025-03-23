package com.rsk

import java.io.Closeable
import java.time.LocalDate

class Meeting : Closeable{
    var Title: String = ""
    var When: LocalDate = LocalDate.MIN
    var Who = mutableListOf<String>()

    fun create(){
        println("Created")
    }
    override fun close() {
        println("Was closed")
    }
}

fun main() {
//    val boardMeeting = Meeting()
//    with(boardMeeting) {
//        Title = "Board Meeting"
//        When = LocalDate.now()
//        Who.add("Kevin")
//    }
//
//    boardMeeting.apply {
//        Title = "Board Meeting"
//        When = LocalDate.now()
//        Who.add("Kevin")
//    }.create()

    Meeting().use {
        it.create()
    }
}
