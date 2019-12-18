// Day 2
package main

import (
	"fmt"

	oc "aoc/helpers/opcodes"
)

func main() {
	opcodes := oc.ReadOpcodesFromFile("./day02-input.txt")

	fmt.Println("Part one:", PartOne(opcodes))
	fmt.Println("Part two:", PartTwo(opcodes))
}
