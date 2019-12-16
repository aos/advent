// Part 2
// What is the fewest combined steps the wires must take to reach an
// intersection?

// NOTE: This code is extremely kludgy... An alternative would be to treat this
// as a graph problem which would make this second part much more elegant as it
// it's just looking for shortest path with the distance between the turns
// (vectors) as our weight
package main

import (
	h "aoc/helpers"
	"log"
	"math"
	"strconv"
)

// PartTwo finds the minimum number of steps to the intersections
func PartTwo(wiresCoords [][]string) int {
	// 1. Get intersections
	intersections := FindIntersections(wiresCoords)
	// 2. For each wire, count number of steps each wire takes to get to
	// each intersection
	intersectMap := make(map[h.Point]bool)
	for i := range intersections {
		if _, ok := intersectMap[intersections[i]]; !ok {
			intersectMap[intersections[i]] = true
		}
	}
	pointStepsMap := make(map[h.Point]int)
	for t := range wiresCoords {
		FindSteps(wiresCoords[t], intersectMap, pointStepsMap)
	}
	// 3. Compare and use lower
	minDistance := math.MaxInt64
	for _, v := range pointStepsMap {
		if v <= minDistance {
			minDistance = v
		}
	}
	return minDistance
}

// FindSteps finds the number of steps a wire takes to each intersection
func FindSteps(w []string, intersectMap map[h.Point]bool, pointSteps map[h.Point]int) map[h.Point]int {
	x, y := 0, 0
	steps := 0
	for _, dot := range w {
		direction := dot[0]
		length, err := strconv.Atoi(dot[1:])
		if err != nil {
			panic(err)
		}

		switch direction {
		case 'U':
			for t := 0; t < length; t++ {
				y++
				steps++
				p := h.Point{X: x, Y: y}
				if intersectMap[p] {
					pointSteps[p] += steps

				}
			}
		case 'D':
			for t := 0; t < length; t++ {
				y--
				steps++
				p := h.Point{X: x, Y: y}
				if intersectMap[p] {
					pointSteps[p] += steps
				}
			}
		case 'L':
			for t := 0; t < length; t++ {
				x--
				steps++
				p := h.Point{X: x, Y: y}
				if intersectMap[p] {
					pointSteps[p] += steps
				}
			}
		case 'R':
			for t := 0; t < length; t++ {
				x++
				steps++
				p := h.Point{X: x, Y: y}
				if intersectMap[p] {
					pointSteps[p] += steps
				}
			}
		default:
			log.Fatal("Invalid direction", direction)
		}

	}

	return pointSteps
}
