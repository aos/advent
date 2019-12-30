package main

import (
	"aoc/helpers/opcodes"
	"fmt"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day13-input.txt")

	fmt.Println("Part one:", PartOne(oc))
	fmt.Println("Part two:", PartTwo(oc))
}
