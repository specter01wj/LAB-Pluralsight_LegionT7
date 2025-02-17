package com.jinwang.myapp_todolist

import androidx.lifecycle.ViewModel
import androidx.compose.runtime.mutableStateListOf

class TaskViewModel : ViewModel() {
    private var nextId = 1
    var tasks = mutableStateListOf<Task>()
        private set

    fun addTask(title: String) {
        if (title.isNotBlank()) {
            tasks.add(Task(id = nextId++, title = title))
        }
    }

    fun toggleTaskCompletion(taskId: Int) {
        tasks.replaceAll { task ->
            if (task.id == taskId) task.copy(isCompleted = !task.isCompleted) else task
        }
    }

    fun removeTask(taskId: Int) {
        tasks.removeAll { it.id == taskId }
    }
}