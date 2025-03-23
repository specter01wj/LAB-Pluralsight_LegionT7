package com.rsk

fun main() {
    println("Started...")

    val logger : Logger = NullLogger()

    val earth = Planet("Earth", 12742, logger)

    println("Planet created: it's name is ${earth.name} and it's radius is ${earth.radius} and it's population is ${earth.population}")

    earth.population = 7_000_000_000
    println("Planet created: it's name is ${earth.name} and it's radius is ${earth.radius} and it's population is ${earth.population}")

//    earth.initPopulationRun()
    earth.runPopulationModel(0, 1000, 100)
    println("New population is: ${earth.population}")

//    val galaxy = SpaceBody("NGC-0001")
}