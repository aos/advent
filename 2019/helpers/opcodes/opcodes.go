package opcodes

import (
	"io/ioutil"
	"strconv"
	"strings"
)

// ReadOpcodesFromFile reads a file with opcodes ("39,29,10") and converts it to an
// integer array
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
func OpcodeVM(o []int, in, out chan int) {
	opcodes := make([]int, len(o))
	copy(opcodes, o)
	pc := 0
	pcMove := 0
	// reader := bufio.NewReader(os.Stdin)

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
			input := <-in
			//if err != nil {
			//	panic(err)
			//}
			//value, err := strconv.Atoi(strings.TrimSpace(in))
			//if err != nil {
			//	panic(err)
			//}
			opcodes[opcodes[pc+1]] = input
			pcMove = 2

		// opcode 4 - outputs value of parameter
		case 4:
			if inst[1] == 0 {
				// fmt.Println(opcodes[opcodes[pc+1]])
				out <- opcodes[opcodes[pc+1]]
			} else {
				out <- opcodes[pc+1]
				//fmt.Println(opcodes[pc+1])
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
