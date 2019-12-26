package main

import (
	"aoc/helpers/opcodes"
	"fmt"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day11-input.txt")
	fmt.Println(oc)
}
