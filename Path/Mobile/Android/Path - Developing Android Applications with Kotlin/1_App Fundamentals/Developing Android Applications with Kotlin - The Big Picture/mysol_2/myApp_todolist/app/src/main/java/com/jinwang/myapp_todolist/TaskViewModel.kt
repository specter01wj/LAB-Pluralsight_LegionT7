package com.jinwang.myapp_todolist

import androidx.compose.runtime.mutableStateListOf
import android.app.Application
import android.content.Context
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch
import org.json.JSONArray
import org.json.JSONObject

class TaskViewModel(application: Application) : AndroidViewModel(application) {
    private val sharedPreferences = application.getSharedPreferences("tasks_prefs", Context.MODE_PRIVATE)
    private var nextId = 1
    var tasks = mutableStateListOf<Task>()
        private set

    init {
        loadTasks()
    }

    fun addTask(title: String) {
        if (title.isNotBlank()) {
            tasks.add(Task(id = nextId++, title = title))
            saveTasks()
        }
    }

    fun toggleTaskCompletion(taskId: Int) {
        tasks.replaceAll { task ->
            if (task.id == taskId) task.copy(isCompleted = !task.isCompleted) else task
        }
        saveTasks()
    }

    fun removeTask(taskId: Int) {
        tasks.removeAll { it.id == taskId }
        saveTasks()
    }

    private fun saveTasks() {
        viewModelScope.launch {
            val jsonArray = JSONArray()
            tasks.forEach { task ->
                val jsonObject = JSONObject()
                jsonObject.put("id", task.id)
                jsonObject.put("title", task.title)
                jsonObject.put("isCompleted", task.isCompleted)
                jsonArray.put(jsonObject)
            }
            sharedPreferences.edit().putString("tasks_list", jsonArray.toString()).apply()
        }
    }

    private fun loadTasks() {
        val jsonString = sharedPreferences.getString("tasks_list", null) ?: return
        val jsonArray = JSONArray(jsonString)
        for (i in 0 until jsonArray.length()) {
            val jsonObject = jsonArray.getJSONObject(i)
            val task = Task(
                id = jsonObject.getInt("id"),
                title = jsonObject.getString("title"),
                isCompleted = jsonObject.getBoolean("isCompleted")
            )
            tasks.add(task)
            nextId = (task.id + 1).coerceAtLeast(nextId)
        }
    }
}