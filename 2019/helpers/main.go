package helpers

import (
	"bufio"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

// Point is an X,Y coordinate location
type Point struct {
	X int
	Y int
}

// SplitComma defines a custom SplitFunc for bufio.Scanner
func SplitComma(data []byte, atEOF bool) (int, []byte, error) {
	for i := 0; i < len(data); i++ {
		if data[i] == ',' {
			return i + 1, data[:i], nil
		}
	}

	return 0, data, bufio.ErrFinalToken
}

// ManhattanDistance calculates the manhattan distances between two Points
func ManhattanDistance(pOne, pTwo Point) int {
	return abs(pOne.X-pTwo.X) + abs(pOne.Y-pTwo.Y)
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

// ReadOpcodesFromFile reads a file with opcodes ("39,29,10") and converts it to an
// integer array
func ReadOpcodesFromFile(f string) []int {
	input, err := ioutil.ReadFile(f)
	if err != nil {
		log.Fatal(err)
	}
	out := strings.Split(strings.TrimSpace(string(input)), ",")
	opcodes := make([]int, len(out))
	for i := range out {
		toInt, err := strconv.Atoi(out[i])
		if err != nil {
			log.Fatal(err)
		}
		opcodes[i] = toInt
	}
	return opcodes
}
