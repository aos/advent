// Part 1
// Before running the program, replace position 1 with the value 12 and replace
// position 2 with the value 2. What value is left at position 0 after the
// program halts?

package main

// PartOne ..
func PartOne(opcodes []int) int {
	opcodesCopy := make([]int, len(opcodes))
	copy(opcodesCopy, opcodes)
	opcodesCopy[1] = 12
	opcodesCopy[2] = 2

	idx := 0
loop:
	for {
		switch opcodesCopy[idx] {
		// opcode 1  - addition
		case 1:
			opcodesCopy[opcodesCopy[idx+3]] =
				opcodesCopy[opcodesCopy[idx+1]] + opcodesCopy[opcodesCopy[idx+2]]

		// opcode 2  - multiplication
		case 2:
			opcodesCopy[opcodesCopy[idx+3]] =
				opcodesCopy[opcodesCopy[idx+1]] * opcodesCopy[opcodesCopy[idx+2]]

		// opcode 99 - halt
		case 99:
			break loop
		}

		idx += 4
	}

	return opcodesCopy[0]
}
