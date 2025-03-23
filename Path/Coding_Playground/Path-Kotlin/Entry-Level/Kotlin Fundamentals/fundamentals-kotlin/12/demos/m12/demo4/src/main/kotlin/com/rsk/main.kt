package com.rsk

fun main() {

    var m1: Meeting? = null
    var m2 = Meeting()

    closeMeeting(m2)
    m1?.let {
        closeMeeting(it)
    }

}

fun closeMeeting(m: Meeting) {
    m.close()
}

class Address

class Meeting {
    lateinit var address: Address

    fun close() {
        println("Meeting closed")

    }

    fun initAddress(addr : Address) {
        address = addr
    }
}


















