package com.rsk

class TestPlanet {

    lateinit var planet: Planet

    fun setup() {
        planet = Planet("" , 0)
    }

    fun test() {
        planet.population
    }
}