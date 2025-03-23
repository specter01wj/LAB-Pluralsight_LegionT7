package com.rsk

class Planet(val name: String, diameter: Int) {
    var population: Long

    init {
        println("We've been created with name: $name")
        population = 0
    }

    val radius: Int = diameter/2


    constructor(name: String, diameter: Int, gaseous: Boolean) : this(name, diameter)
    constructor(name: String, diameter: Int, gaseous: Boolean, hasLife: Boolean) : this(name, diameter)

    private fun initPopulationRun(startDate: Int, endDate: Int, startPopulation: Int) {
        // do some work
    }

    fun runPopulationModel(startDate: Int, endDate: Int, startPopulation: Int) : Long {
        initPopulationRun(startDate, endDate, startPopulation)
        return population
    }
}