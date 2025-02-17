package com.jinwang.myapp_todolist

data class Task(
    val id: Int,
    val title: String,
    val isCompleted: Boolean = false
)