package com.rsk

fun main() {
    val o = Organizer()

    o.closeMeeting(Meeting())
    o.closeNullableMeeting(Meeting())
    o.closeNullableMeeting(null)
}

class Organizer {
    fun closeMeeting(m: Meeting) {
        m.close()
    }

    fun closeNullableMeeting(m: Meeting?) {
        m?.close()
    }

}

class Meeting{
    fun close() {
        println("Meeting closed")
    }
}
