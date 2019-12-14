// Part 1
// How many different passwords meet the following criteria:
/*
- It is a six-digit number.
- The value is within the range given in your puzzle input.
- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase
or stay the same (like 111123 or 135679).
*/

package main

// PartOne tests all digits in the range given
func PartOne(n int) bool {
	last := n % 10
	n /= 10
	meeting := false

	for i := 0; i < 5; i++ {
		digit := n % 10
		n /= 10

		if last < digit {
			return false
		}

		if last == digit {
			meeting = true
		}

		last = digit
	}

	return meeting
}
