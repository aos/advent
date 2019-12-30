package main

import (
	"aoc/helpers/opcodes"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day13-input.txt")

	// fmt.Println("Part one:", PartOne(oc))
	PartTwo(oc)
}
