package com.rsk

@JvmInline
value class Score(val score: Int) {
    init {
        if(score < 0 || score > 100) throw IllegalArgumentException()
    }
}

class Exam {
    fun score(name: String, studentScore: Score) {

        // ...
    }

    fun amendScore(id: Int, newScore: Score) {
    }
}

fun main() {
}