package com.rsk

sealed class PersonEvents(val id: Int) {
    class Awake(id: Int): PersonEvents(id)
    class Asleep(id: Int): PersonEvents(id)
    class Eating(id: Int, val food: String) : PersonEvents(id)
}

class Cooking(id: Int) : PersonEvents(id)

fun main() {
    val evt = PersonEvents.Awake(1)

    handlePersonEvent(evt)

    val evt1 = PersonEvents.Eating(23, "Nuts")
    handlePersonEvent(evt1)
}

fun handlePersonEvent(evt: PersonEvents) {
    when(evt) {
        is PersonEvents.Awake -> { println("Awake: ${evt.id}")}
        is PersonEvents.Asleep -> {}
        is PersonEvents.Eating -> {
            println("Eating: ${evt.id}, ${evt.food}")
        }
        is Cooking -> {}
    }
}