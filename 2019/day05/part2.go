// Part 2
// What is the diagnostic code for system ID 5?
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// PartTwo ...
func PartTwo(o []int) {
	opcodes := make([]int, len(o))
	copy(opcodes, o)
	pc := 0
	pcMove := 0
	reader := bufio.NewReader(os.Stdin)

loop:
	for {
		inst := parseInstruction(opcodes[pc])
		paramOne, paramTwo := setParams(opcodes, inst, pc)
		switch inst[0] {
		// opcode 1 - addition
		// opcode 2 - multiplication
		case 1, 2:
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
			if inst[1] == 0 {
				fmt.Println(opcodes[opcodes[pc+1]])
			} else {
				fmt.Println(opcodes[pc+1])
			}
			pcMove = 2

		// opcode 5 - jump-if-true
		// opcode 6 - jump-if-false
		case 5, 6:
			if res, ok := applyJump(inst[0], paramOne, paramTwo); ok {
				pc = res
				continue loop
			}
			pcMove = 3

		// opcode 7 - less than
		// opcode 8 - equals
		case 7, 8:
			opcodes[opcodes[pc+3]] =
				applyCompare(inst[0], paramOne, paramTwo)
			pcMove = 4

		// opcode 99 - halt
		case 99:
			break loop
		}

		pc += pcMove
	}
}

func applyJump(n, p1, p2 int) (int, bool) {
	switch n {
	case 5:
		if p1 != 0 {
			return p2, true
		}

	case 6:
		if p1 == 0 {
			return p2, true
		}
	}
	return -1, false
}

func applyCompare(n, p1, p2 int) int {
	switch n {
	case 7:
		if p1 < p2 {
			return 1
		}

	case 8:
		if p1 == p2 {
			return 1
		}
	}
	return 0
}

func setParams(opcodes, inst []int, pc int) (int, int) {
	paramOne := 0
	paramTwo := 0

	switch inst[0] {
	case 1, 2, 5, 6, 7, 8:
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
	default:
		paramOne, paramTwo = 0, 0
	}

	return paramOne, paramTwo
}
