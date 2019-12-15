// Day 2
package main

import (
	"fmt"

	"aoc/helpers"
)

func main() {
	opcodes := helpers.ReadOpcodesFromFile("./day02-input.txt")

	fmt.Println("Part one:", PartOne(opcodes))
	fmt.Println("Part two:", PartTwo(opcodes))
}
