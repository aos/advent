package main

import (
	"aoc/helpers/opcodes"
	"fmt"
	"sync"
)

type safeHighest struct {
	num int
	mux sync.Mutex
}

// PartTwo ...
func PartTwo(oc []int) {
	perms := createPermutations(5, 9)
	highest := safeHighest{num: -1}

	for _, perm := range perms {
		ins := make([]chan int, len(perm))
		outs := make([]chan int, len(perm))
		dones := make([]chan bool, len(perm))

		for i, val := range perm {
			in := make(chan int, 1)
			out, done := opcodes.OpcodeVM(oc, in)

			in <- val
			if i == 0 {
				in <- 0
			}

			ins[i] = in
			outs[i] = out
			dones[i] = done
		}

		var wg sync.WaitGroup
		wg.Add(len(ins))

		for j := range ins {
			go func(idx int) {
				defer wg.Done()

				oldIdx := idx - 1
				if idx == 0 {
					oldIdx = len(ins) - 1
				}

				// Listen on old output channel and feed into
				// next input channel
				for val := range outs[oldIdx] {
					select {
					case <-dones[idx]:
						highest.mux.Lock()
						if val > highest.num {
							highest.num = val
						}
						highest.mux.Unlock()
						return
					default:
						ins[idx] <- val
					}

				}
			}(j)
		}
		wg.Wait()
	}
	fmt.Println("Part two:", highest.num)
}
