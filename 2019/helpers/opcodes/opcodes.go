package opcodes

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

// ReadOpcodesFromFile reads a file with opcodes ("39,29,10") and converts it
// to an integer array
func ReadOpcodesFromFile(f string) []int {
	input, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(input)), ",")
	opcodes := make([]int, len(out))
	for i := range out {
		toInt, err := strconv.Atoi(out[i])
		if err != nil {
			panic(err)
		}
		opcodes[i] = toInt
	}
	return opcodes
}

// OpcodeVM is the VM that takes in opcodes and runs them
func OpcodeVM(o []int, in chan int) (chan int, chan bool) {
	opcodes := make([]int, math.MaxInt16)
	copy(opcodes, o)
	out := make(chan int)
	done := make(chan bool, 1)

	go func() {
		pc := 0
		pcMove := 0
		relBase := 0
	loop:
		for {
			inst := parseInstruction(opcodes[pc])
			paramOne, paramTwo, paramThree :=
				setParams(opcodes, inst, pc, relBase)
			switch inst[0] {
			// opcode 1 - addition
			// opcode 2 - multiplication
			case 1, 2:
				opcodes[paramThree] =
					applyAddMult(inst[0], paramOne, paramTwo)
				pcMove = 4

			// opcode 3 - takes integer input, saves to position
			case 3:
				idx := opcodes[pc+1]
				if inst[1] == 2 {
					idx += relBase
				}
				opcodes[idx] = <-in
				pcMove = 2

			// opcode 4 - outputs value of parameter
			case 4:
				out <- paramOne
				pcMove = 2

			// opcode 5 - jump-if-true
			// opcode 6 - jump-if-false
			case 5, 6:
				if res, ok :=
					applyJump(inst[0], paramOne, paramTwo); ok {
					pc = res
					continue loop
				}
				pcMove = 3

			// opcode 7 - less than
			// opcode 8 - equals
			case 7, 8:
				opcodes[paramThree] =
					applyCompare(inst[0], paramOne, paramTwo)
				pcMove = 4

			// opcode 9 - adjust relative base offset
			case 9:
				relBase += paramOne
				pcMove = 2

			// opcode 99 - halt
			case 99:
				done <- true
				close(out)
				return

			default:
				fmt.Printf(
					"error: failed to match intcode: %d\n",
					inst)
				done <- true
				close(out)
				return
			}

			pc += pcMove
		}

	}()
	return out, done
}

func parseInstruction(n int) []int {
	// [instruction, mode of 1st param, mode of 2nd param, ...]
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

func applyJump(n, p1, p2 int) (int, bool) {
	if n == 5 && p1 != 0 {
		return p2, true
	}
	if n == 6 && p1 == 0 {
		return p2, true
	}
	return -1, false
}

func applyCompare(n, p1, p2 int) int {
	if n == 7 && p1 < p2 {
		return 1
	}
	if n == 8 && p1 == p2 {
		return 1
	}
	return 0
}

func setParams(opcodes, inst []int, pc, base int) (int, int, int) {
	paramOne := 0
	paramTwo := 0
	paramThree := 0

	switch inst[0] {
	case 1, 2, 4, 5, 6, 7, 8, 9:
		if inst[1] == 0 {
			// Parameter mode = 0
			paramOne = opcodes[opcodes[pc+1]]
		} else if inst[1] == 1 {
			paramOne = opcodes[pc+1]
			// Immediate mode = 1
		} else {
			// Relative mode  = 2
			idx := base + opcodes[pc+1]
			paramOne = opcodes[idx]
		}

		if inst[2] == 0 {
			paramTwo = opcodes[opcodes[pc+2]]
		} else if inst[2] == 1 {
			paramTwo = opcodes[pc+2]
		} else {
			idx := base + opcodes[pc+2]
			paramTwo = opcodes[idx]
		}

		if inst[3] == 0 {
			paramThree = opcodes[pc+3]
		} else if inst[3] == 1 {
			paramThree = pc + 3
		} else {
			paramThree = base + opcodes[pc+3]
		}
	default:
		paramOne, paramTwo, paramThree = 0, 0, 0
	}

	return paramOne, paramTwo, paramThree
}
