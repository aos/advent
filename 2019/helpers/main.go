package helpers

import (
	"bufio"
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
