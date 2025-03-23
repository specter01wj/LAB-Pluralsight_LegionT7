package com.rsk

fun padding(original: String, numberToReplace: Int, replacementChar: Char = ' '): String {
    val strToAdd = replacementChar.toString().repeat(numberToReplace)
    return original + strToAdd
}

fun String.pad(numberToReplace: Int, replacementChar: Char = ' '): String {
    val strToAdd = replacementChar.toString().repeat(numberToReplace)
    return this + strToAdd
}

fun main() {
    val original = "Kevin"
    val newStr = padding(original, 5)
    println("***${newStr}***")

    val newerString = original.pad(4)

    println("***${newerString}***")
}

