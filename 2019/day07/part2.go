package main

import (
	"aoc/helpers/opcodes"
	"fmt"
	"math"
)

// PartTwo ...
func PartTwo(oc []int) {
	perms := createPermutations(5, 9)
	signals := make(chan int, len(perms))

	for i := range perms {
		in := make(chan int, 2)
		out := make(chan int, 1)
		in <- perms[i][0]
		in <- 0
		opcodes.OpcodeVM(oc, in, out)

		settings := []int{
			perms[i][1],
			perms[i][2],
			perms[i][3],
			perms[i][4],
		}
		for j := range settings {
			in <- settings[j]
			in <- (<-out)
			opcodes.OpcodeVM(oc, in, out)
		}

		in <- (<-out)
		opcodes.OpcodeVM(oc, in, in)
		close(in)
		close(out)
		signals <- (<-out)
	}
	close(signals)

	max := math.MinInt64
	for p := range signals {
		if p > max {
			max = p
		}
	}
	fmt.Println(max)
}
