// Part 2
// Additional criteria:
// - the two adjacent matching digits are not part of a larger group of
// matching digits
package main

// PartTwo solves the second part of the problem
func PartTwo(n int) bool {
	last := n % 10
	n /= 10
	adjacent := 0
	met := false
	metWith := 0

	for i := 0; i < 5; i++ {
		digit := n % 10
		n /= 10

		if last < digit {
			return false
		}

		if last == digit {
			adjacent++
		} else {
			adjacent = 0
		}

		if adjacent == 1 && !met {
			met = true
			metWith = digit
		}

		if adjacent > 1 && metWith == digit {
			met = false
			metWith = 0
		}

		last = digit
	}

	return met
}
