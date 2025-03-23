package com.rsk

data class Point(val x: Int, val y: Int) {
}

infix fun Point.add(point: Point) = Point(this.x + point.x, this.y + point.y)
operator fun Point.plus(point: Point) = Point(this.x + point.x, this.y + point.y)


fun main() {
    val pt1 = Point(1, 1)
    val pt2 = Point(2, 2)

//    val newPt = pt1.add(pt2)
//    val newPt = pt1 add pt2
    val newPt = pt1 + pt2

    println(newPt)

}

