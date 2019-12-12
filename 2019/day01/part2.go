// Part 2
// Recursively calculate module fuel cost

package main

import (
	"bufio"
	"io"
	"log"
	"strconv"
)

var cache = make(map[int]int)

// PartTwo ...
func PartTwo(f io.Reader) int {
	sum := 0
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		module := scanner.Text()
		i, err := strconv.Atoi(module)

		if err != nil {
			log.Fatal(err)
		}

		sum += calculateModuleTotalFuel(i)
	}

	return sum
}

func calculateModuleTotalFuel(mass int) int {
	fuel := cache[mass]

	if fuel == 0 {
		fuel = (mass / 3) - 2
	}

	if fuel <= 0 {
		return 0
	}

	cache[mass] = fuel
	return fuel + calculateModuleTotalFuel(fuel)
}
