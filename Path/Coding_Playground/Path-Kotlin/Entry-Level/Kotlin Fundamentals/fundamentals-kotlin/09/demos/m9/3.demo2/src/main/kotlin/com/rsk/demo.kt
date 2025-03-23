package com.rsk

fun padding(original: String, numberToReplace: Int, replacementChar: Char = ' '): String {
    val strToAdd = replacementChar.toString().repeat(numberToReplace)
    return original + strToAdd
}

fun addPlayer(name: String, highScore: Int, lowScore: Int, totalScore: Int = 1000) {

}

//fun addPlayer(name: String, highScore: Int, lowScore: Int) {
//    addPlayer(name, highScore, lowScore, 1000)
//}

fun addPlayer(firstName: String, lastName: String, highScore: Int, lowScore: Int, totalScore: Int = 1000) {
    addPlayer("$firstName $lastName", highScore, lowScore, totalScore)
}


fun main() {
    val original = "Kevin"
    val newStr = padding(original, 5)

    println("***${newStr}***")

    addPlayer("Kevin", lowScore = 0, highScore = 100)
}

