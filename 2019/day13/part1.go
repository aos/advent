// Part 1
package main

import "aoc/helpers/opcodes"

// PartOne ...
func PartOne(oc []int) int {
	out, _ := opcodes.OpcodeVM(oc, nil)

	// Part 1
	num := 0
	blocks := 0
	for d := range out {
		num++
		if num == 3 {
			num = 0
			if d == 2 {
				blocks++
			}
		}
	}
	return blocks
}
