package helpers

import (
	"bufio"
	"math"
)

// Min is an integer variadic min function
func Min(n ...int) int {
	min := math.MaxInt64
	for i := range n {
		if n[i] <= min {
			min = n[i]
		}
	}
	return min
}

// Abs is an integer version of absolute value
func Abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
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
