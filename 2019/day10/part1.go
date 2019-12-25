// Part 1
package main

import (
	"aoc/helpers/geo"
)

// PartOne ...
func PartOne(asts []geo.Point) (geo.Point, int) {
	asteroids := make(map[geo.Point]int)
	for k := range asts {
		quadrants := make(map[int]map[float64]bool)
		for j := range asts {
			// Same point
			if asts[k] == asts[j] {
				continue
			}
			d := asts[k].AdjacentPointDirection(asts[j])
			if quadrants[d] == nil {
				quadrants[d] = make(map[float64]bool)
			}
			s := geo.SlopeOfPoints(asts[k], asts[j])
			if _, ok := quadrants[d][s]; !ok {
				quadrants[d][s] = true
			}
		}
		for q := range quadrants {
			asteroids[asts[k]] += len(quadrants[q])
		}
	}

	largest := -1
	var p geo.Point
	for k, n := range asteroids {
		if n > largest {
			largest = n
			p = k
		}
	}
	return p, largest
}
