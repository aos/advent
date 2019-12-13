package main

import (
	. "aoc/helpers"
	"log"
	"math"
	"strconv"
)

// Wire contains the Point coordinates tracing set for a wire
type Wire map[Point]bool

// Intersect finds the points where two wires cross
func (w Wire) Intersect(other Wire) []Point {
	var res []Point
	for k := range w {
		if _, ok := other[k]; ok {
			res = append(res, k)
		}
	}
	return res
}

// PartOne finds the Manhattan distance between Wires
func PartOne(wiresCoords [][]string) int {
	wires := make([]Wire, len(wiresCoords))
	for i := range wiresCoords {
		wires[i] = TraceWireOnMap(wiresCoords[i])
	}
	intersect := wires[0].Intersect(wires[1])

	minDistance := math.MaxInt64
	for ix := range intersect {
		d := ManhattanDistance(intersect[ix], Point{X: 0, Y: 0})
		if d < minDistance {
			minDistance = d
		}
	}

	return minDistance
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
				wire[Point{X: x, Y: y + t}] = true
			}
			y += length
		case 'D':
			for t := 0; t < length+1; t++ {
				wire[Point{X: x, Y: y - t}] = true
			}
			y -= length
		case 'L':
			for t := 0; t < length+1; t++ {
				wire[Point{X: x - t, Y: y}] = true
			}
			x -= length
		case 'R':
			for t := 0; t < length+1; t++ {
				wire[Point{X: x + t, Y: y}] = true
			}
			x += length
		default:
			log.Fatal("Invalid direction", direction)
		}

	}
	// Does not count towards intersection
	delete(wire, Point{X: 0, Y: 0})
	return wire
}
