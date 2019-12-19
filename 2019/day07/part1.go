package main

import (
	"aoc/helpers/opcodes"
	"fmt"
	"math"
	"sync"
)

// PartOne ...
func PartOne(oc []int) {
	perms := createPermutations(0, 4)
	signals := make(chan int, len(perms))
	sendWork := make(chan []int)

	var wg sync.WaitGroup
	workers := 3
	wg.Add(workers)

	// Parallelize this
	for i := 0; i < workers; i++ {
		go func() {
			for perm := range sendWork {
				in := make(chan int, 2)
				out := make(chan int, 1)
				in <- perm[0]
				in <- 0
				opcodes.OpcodeVM(oc, in, out)

				settings := []int{
					perm[1],
					perm[2],
					perm[3],
					perm[4],
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
			wg.Done()
		}()
	}

	max := math.MinInt64
	go func() {
		for p := range signals {
			if p > max {
				max = p
			}
		}
	}()

	for i := range perms {
		sendWork <- perms[i]
	}
	close(sendWork)

	wg.Wait()
	close(signals)

	fmt.Println(max)
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
