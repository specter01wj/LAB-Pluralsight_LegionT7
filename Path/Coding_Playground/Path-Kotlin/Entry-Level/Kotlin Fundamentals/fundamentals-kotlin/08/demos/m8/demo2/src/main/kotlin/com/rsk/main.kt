package com.rsk

fun main() {
    val window = Window()

    window.addMouseListener(object: MouseListener{
        override fun mouseClicked(e: MouseEvent) {

        }

        override fun mouseEntered(e: MouseEvent) {
            
        }
    })
}

class Window {
    fun addMouseListener(listener: MouseListener) {}
}

interface MouseListener {
    fun mouseClicked(e: MouseEvent)
    fun mouseEntered(e: MouseEvent)
}

class MouseEvent {

}

