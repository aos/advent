// Day 9
package main

import (
	"aoc/helpers/opcodes"
	"fmt"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day09-input.txt")
	in := make(chan int, 1)

	// Part 1
	in <- 1
	out, _ := opcodes.OpcodeVM(oc, in)
	for i := range out {
		fmt.Println("Part one:", i)
	}

	// Part 2
	in <- 2
	out, _ = opcodes.OpcodeVM(oc, in)
	fmt.Println("Part two:", <-out)
}
