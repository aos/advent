// Part 1
// What is the Manhattan distance from the central port to the closest
// intersection?
package main

import (
	h "aoc/helpers"
	"log"
	"math"
	"strconv"
)

// Wire contains the Point coordinates tracing set for a wire
type Wire map[h.Point]bool

// Intersect finds the points where two wires cross
func (w Wire) Intersect(other Wire) []h.Point {
	var res []h.Point
	for k := range w {
		if _, ok := other[k]; ok {
			res = append(res, k)
		}
	}
	return res
}

// PartOne finds the Manhattan distance between Wires
func PartOne(wiresCoords [][]string) int {
	intersect := FindIntersections(wiresCoords)
	minDistance := math.MaxInt64
	for ix := range intersect {
		d := h.ManhattanDistance(intersect[ix], h.Point{X: 0, Y: 0})
		if d < minDistance {
			minDistance = d
		}
	}

	return minDistance
}

// FindIntersections returns an array of the intersecting points given wire
// coordinates
func FindIntersections(wiresCoords [][]string) []h.Point {
	wires := make([]Wire, len(wiresCoords))
	for i := range wiresCoords {
		wires[i] = TraceWireOnMap(wiresCoords[i])
	}
	intersectingWires := wires[0].Intersect(wires[1])
	return intersectingWires
}

// TraceWireOnMap creats a Wire set with all the points
func TraceWireOnMap(w []string) Wire {
	wire := make(Wire)
	x, y := 0, 0
	for _, dot := range w {
		direction := dot[0]
		length, err := strconv.Atoi(dot[1:])
		if err != nil {
			panic(err)
		}

		switch direction {
		case 'U':
			for t := 0; t < length+1; t++ {
				wire[h.Point{X: x, Y: y + t}] = true
			}
			y += length
		case 'D':
			for t := 0; t < length+1; t++ {
				wire[h.Point{X: x, Y: y - t}] = true
			}
			y -= length
		case 'L':
			for t := 0; t < length+1; t++ {
				wire[h.Point{X: x - t, Y: y}] = true
			}
			x -= length
		case 'R':
			for t := 0; t < length+1; t++ {
				wire[h.Point{X: x + t, Y: y}] = true
			}
			x += length
		default:
			log.Fatal("Invalid direction", direction)
		}

	}
	// Does not count towards intersection
	delete(wire, h.Point{X: 0, Y: 0})
	return wire
}
