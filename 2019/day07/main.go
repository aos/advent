package main

import (
	"aoc/helpers/opcodes"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day07-input.txt")
	PartOne(oc)
	PartTwo(oc)
}
