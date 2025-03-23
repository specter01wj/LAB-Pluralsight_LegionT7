package com.rsk


// override toString
data class Person(val name: String) {
    var age: Int = 0

    override fun toString(): String {
        return "Person(name=$name, age=$age)"
    }
}

fun main() {

    val sam = Person("Sam")
    sam.age = 31
    val samuel = Person("Sam")
    samuel.age = 32

    println("$sam, has hashCode ${sam.hashCode()}")
    println("$samuel, has hashCode ${samuel.hashCode()}")

    if(sam.equals(samuel)) {
        println("these are the same")
    }

}