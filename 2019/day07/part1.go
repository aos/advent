package main

import (
	"aoc/helpers/opcodes"
	"fmt"
)

// PartOne ...
func PartOne(oc []int) {
	perms := createPermutations(0, 4)
	signals := make(chan int, len(perms))
	in := make(chan int, 2)
	for i := range perms {
		in <- perms[i][0]
		in <- 0
		out, _ := opcodes.OpcodeVM(oc, in)

		settings := []int{
			perms[i][1],
			perms[i][2],
			perms[i][3],
			perms[i][4],
		}
		for j := range settings {
			in = make(chan int, 2)
			in <- settings[j]
			in <- (<-out)
			out, _ = opcodes.OpcodeVM(oc, in)
		}
		signals <- (<-out)
	}

	max := -1
	close(signals)
	for s := range signals {
		if s > max {
			max = s
		}
	}
	fmt.Println("Part one:", max)
}

func createPermutations(first, last int) [][]int {
	var perms [][]int
	for a := first; a <= last; a++ {
		for b := first; b <= last; b++ {
			for c := first; c <= last; c++ {
				for d := first; d <= last; d++ {
					for e := first; e <= last; e++ {
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
