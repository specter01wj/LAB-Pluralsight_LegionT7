package com.rsk

fun main() {

    var m1 : Meeting? = null
    var m2 = Meeting()

    m2 = m1 ?: Meeting()

    m2.close()

    val saveable = m2 as? ISaveable

    saveable?.save()
}

interface ISaveable {
    fun save()
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
