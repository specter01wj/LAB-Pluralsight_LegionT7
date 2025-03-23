package com.rsk

class Meeting {

    @JvmField
    val title = "Board"

    companion object {
        @JvmStatic
        fun build() : Meeting {
            println("building...")
            return Meeting()
        }
    }

}
