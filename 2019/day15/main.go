package main

import (
	"aoc/helpers/geo"
	"aoc/helpers/opcodes"
	"fmt"
)

const (
	north int = iota + 1
	south
	west
	east
)

func main() {
	// Instructions executed in this order:
	// 1. accept/send movement via input:
	//	N
	//	1
	//  W 3 + 4 E
	//	2
	//	S
	// 2. wait for movement to finish
	// 3. output status:
	//	- 0: wall
	//	- 1: moved one step in direction
	//	- 2: moved one step, new position is oxygen system

	oc := opcodes.ReadOpcodesFromFile("input.txt")

	in := make(chan int, 1)
	out, _ := opcodes.OpcodeVM(oc, in)

	visited := make(map[geo.Point]bool)
	walls := make(map[geo.Point]bool)

	in <- north
	x, y := 25, 24
	trace := []int{north}

	for status := range out {
		fmt.Printf("status: %d\n", status)
		switch status {
		case 0: // wall
			walls[geo.Point{x, y}] = true

		case 1: // moved
			visited[geo.Point{x, y}] = true
			x, y = move(north, x, y, in)

		case 2: // arrived

		}
	}
}

func move(dir, curX, curY int, in chan int) (int, int) {
	switch dir {
	case north:
		curY--
	case south:
		curY++
	case west:
		curX--
	case east:
		curX++
	}
	in <- dir
	return curX, curY
}

func oppositeDir(dir int) int {
	switch dir {
	case north:
		return south
	case south:
		return north
	case west:
		return east
	case east:
		return west
	}
	return 0
}

func draw() {
	// Draw the map
}
