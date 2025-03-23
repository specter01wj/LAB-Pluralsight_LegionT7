package com.rsk

fun main() {
    val people = HashMap<String, Int>()

    people["Sam"] = 31
    people["Alex"] = 31
    people["Harry"] = 33

    for((name, age) in people) {
        println("$name is $age")
    }
    
}

fun overArray() {
    val nums = arrayOf(1, 5, 7, 8, 19, 34)

    for(num in nums) {
        println("Number: $num")
    }

    for((index, num) in nums.withIndex()){
        println("Number: $num at $index")
    }

}

fun ranges() {
    var numbers = 1..10

    // for(int i = 0; i < 10; i++) {}

    for (i in 1..10) {
        println("i is $i")
    }

    for (i in 1..10 step 2) {
        println("(step) i is $i")
    }

    for (i in 10 downTo 1) {
        println("(down) i is $i")
    }

    for (i in 0 until 10) {
        println("(until) i is $i")
    }

}