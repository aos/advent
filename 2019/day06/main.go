// Day 6
package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	orbits := make(map[string]string)
	in, err := ioutil.ReadFile("./day06-input.txt")
	if err != nil {
		panic(err)
	}
	out := strings.Split(strings.TrimSpace(string(in)), "\n")
	for i := range out {
		local := strings.Split(out[i], ")")
		orbits[local[1]] = local[0]
	}

	total, sumOrbs := sumPath(orbits)
	fmt.Println("Part one:", total)

	lca, err := findLowestCommonAncestor(orbits)
	if err == nil {
		fmt.Println("Part two:",
			sumOrbs["YOU"]+sumOrbs["SAN"]-(2*sumOrbs[lca]))
	}
}

func sumPath(orbits map[string]string) (int, map[string]int) {
	total := 0
	cache := make(map[string]int)

	for k, v := range orbits {
		if res, ok := cache[v]; ok {
			total += res + 1
			cache[k] = res + 1
			continue
		}

		inner := 0
		for i := k; orbits[i] != "COM"; i = orbits[i] {
			total++
			inner++
		}
		cache[k] = inner + 1
		total++
	}
	return total, cache
}

func findLowestCommonAncestor(orbits map[string]string) (string, error) {
	var youPath []string
	var santaPath []string

	// Trace paths to root
	for i := orbits["YOU"]; orbits[i] != "COM"; i = orbits[i] {
		youPath = append(youPath, i)
	}
	for i := orbits["SAN"]; orbits[i] != "COM"; i = orbits[i] {
		santaPath = append(santaPath, i)
	}

	// Array reverse
	for i := len(santaPath)/2 - 1; i >= 0; i-- {
		opp := len(santaPath) - 1 - i
		santaPath[i], santaPath[opp] = santaPath[opp], santaPath[i]
	}
	for i := len(youPath)/2 - 1; i >= 0; i-- {
		opp := len(youPath) - 1 - i
		youPath[i], youPath[opp] = youPath[opp], youPath[i]
	}

	// Find LCA
	for i := 0; i < len(youPath) && i < len(santaPath); i++ {
		if youPath[i] != santaPath[i] {
			return youPath[i], nil
		}
	}

	return "404", errors.New("Check your input")
}
