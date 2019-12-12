// Day 1 - Puzzle 1
// What is the sum of the fuel requirements for all of the modules on your
// spacecraft? fuel = floor(mass / 3) - 2

package main

import (
	"bufio"
	"io"
	"log"
	"strconv"
)

// PartOne ...
func PartOne(f io.Reader) int {
	sum := 0
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		module := scanner.Text()
		i, err := strconv.Atoi(module)

		if err != nil {
			log.Fatal(err)
		}

		sum += (i / 3) - 2
	}

	return sum
}
