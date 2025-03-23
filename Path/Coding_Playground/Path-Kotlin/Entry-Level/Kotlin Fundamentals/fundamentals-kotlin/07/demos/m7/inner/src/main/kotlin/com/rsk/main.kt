package com.rsk

class Outer {
    val name: String = "Kevin";
    inner class Inner {
        fun doSomething(){
            println(name)
        }
    }
}

val nested = Outer().Inner()
fun main() {
    nested.doSomething()
}

