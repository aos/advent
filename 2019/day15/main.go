package main

import (
	"aoc/helpers/opcodes"
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

	in := make(chan int)
	out, done := opcodes.OpcodeVM(oc, in)
}

func draw() {
	// Draw the map
}
