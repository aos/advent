package main

func main() {
}

func translate(opcodes []int) int {
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
