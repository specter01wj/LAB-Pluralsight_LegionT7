# Demos

## Install

### Command Lin3
1. Install kotlin with homebrew
1. Show the REPL (`2+2` and `println("Hello, World")`)
1. Create `Hello.kt` in an editor
1. `kotlinc Hello.kt`
1. `kotlinc Hello.kt -include-runtime -d hello.jar`
1. `java -jar  hello.jar`

### IntelliJ
1. Show the plugin

## Basic Intro
1. Create a project
1. Create a file (`Hello.kt`)
1. Add a `main`
1. Run it from the IDE
1. Add a run configuration to IntelliJ - class is `MainKt`


    val nums = arrayOf(1)
    val answer = try {
        nums[1]
    } catch (e: Throwable) {
        null
    } 



