// Part 1
// After providing 1 to the only input instruction and passing all the tests,
// what diagnostic code does the program produce?
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// PartOne ...
func PartOne(o []int) {
	opcodes := make([]int, len(o))
	copy(opcodes, o)
	pc := 0
	pcMove := 0
	paramOne := 0
	paramTwo := 0
	reader := bufio.NewReader(os.Stdin)

loop:
	for {
		inst := parseInstruction(opcodes[pc])
		switch inst[0] {
		// opcode 1 - addition
		// opcode 2 - multiplication
		case 1, 2:
			if inst[1] == 0 {
				paramOne = opcodes[opcodes[pc+1]]
			} else {
				paramOne = opcodes[pc+1]
			}

			if inst[2] == 0 {
				paramTwo = opcodes[opcodes[pc+2]]
			} else {
				paramTwo = opcodes[pc+2]
			}

			opcodes[opcodes[pc+3]] =
				applyAddMult(inst[0], paramOne, paramTwo)
			pcMove = 4

		// opcode 3 - takes integer input, saves to position @ parameter
		case 3:
			in, err := reader.ReadString('\n')
			if err != nil {
				panic(err)
			}
			value, err := strconv.Atoi(strings.TrimSpace(in))
			if err != nil {
				panic(err)
			}
			opcodes[opcodes[pc+1]] = value
			pcMove = 2

		// opcode 4 - outputs value of parameter
		case 4:
			fmt.Println(opcodes[opcodes[pc+1]])
			pcMove = 2

		// opcode 99 - halt
		case 99:
			break loop
		}

		pc += pcMove
		paramOne = 0
		paramTwo = 0
	}
}

func parseInstruction(n int) []int {
	inst := make([]int, 4)
	inst[0] = n % 100
	n /= 100
	for i := 1; i < 4; i++ {
		inst[i] = n % 10
		n /= 10
	}
	return inst
}

func applyAddMult(n, p1, p2 int) int {
	if n == 1 {
		return p1 + p2
	}

	return p1 * p2
}
