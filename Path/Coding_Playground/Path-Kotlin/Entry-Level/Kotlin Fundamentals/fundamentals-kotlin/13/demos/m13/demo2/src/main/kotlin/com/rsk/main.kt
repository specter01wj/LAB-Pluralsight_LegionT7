package com.rsk

import com.rsk.java.Meeting

fun main() {
     val m = Meeting()

//    val title: String? = m.meetingTitle
//
//    println(title)

//    m.addTitle("Title")

    val title2 = m.titleCanBeNull()

    val size = title2?.length

    println("Title2: $title2")
}