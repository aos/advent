package main

import (
	"aoc/helpers/opcodes"
	"fmt"
	"math"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day07-input.txt")
	perms := createPermutations()
	signals := make(chan int, len(perms))
	// Parallelize this
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

func createPermutations() [][]int {
	var perms [][]int
	for a := 0; a < 5; a++ {
		for b := 0; b < 5; b++ {
			for c := 0; c < 5; c++ {
				for d := 0; d < 5; d++ {
					for e := 0; e < 5; e++ {
						if a != b &&
							a != c &&
							a != d &&
							a != e &&
							b != c &&
							b != d &&
							b != e &&
							c != d &&
							c != e &&
							d != e {

							perms = append(
								perms,
								[]int{a, b, c, d, e})
						}
					}
				}
			}
		}
	}

	return perms
}
