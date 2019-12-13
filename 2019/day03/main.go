package main

import (
	. "aoc/helpers"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

// Wire contains the tracing for a wire
type Wire map[Point]bool

func (w Wire) Intersect(other Wire) []Point {
	var res []Point
	for k := range w {
		if _, ok := other[k]; ok {
			res = append(res, k)
		}
	}
	return res
}

func main() {
	in, err := os.Open("./day03-input.txt")
	if err != nil {
		panic(err)
	}
	wiresCoords := parseInput(in)
	wires := make([]Wire, len(wiresCoords))
	for i := range wiresCoords {
		wires[i] = traceWireOnMap(wiresCoords[i])
	}
	intersect := wires[0].Intersect(wires[1])

	minDistance := math.MaxInt64
	for ix := range intersect {
		d := ManhattanDistance(intersect[ix], Point{X: 0, Y: 0})
		if d < minDistance {
			minDistance = d
		}
	}
	// Solution to part 1 (!)
	fmt.Println(minDistance)
}

func parseInput(f io.Reader) [][]string {
	in, err := ioutil.ReadAll(f)
	if err != nil {
		log.Fatal(err)
	}

	out := strings.Split(strings.TrimSpace(string(in)), "\n")
	wires := make([][]string, len(out))
	for i := range out {
		wires[i] = strings.Split(string(out[i]), ",")
	}
	return wires
}

func traceWireOnMap(w []string) Wire {
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
