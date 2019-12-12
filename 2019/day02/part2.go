// Part 2
// Find the input noun and verb that cause the program to produce the output
// 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2,
// the answer would be 1202.)

package main

// PartTwo ..
func PartTwo(opcodes []int) int {
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			opcodesCopy := make([]int, len(opcodes))
			copy(opcodesCopy, opcodes)

			opcodesCopy[1] = noun
			opcodesCopy[2] = verb

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

			if opcodesCopy[0] == 19690720 {
				return 100*opcodesCopy[1] + opcodesCopy[2]
			}
		}

	}

	return 0
}
