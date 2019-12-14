// Day 3
package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func main() {
	in, err := os.Open("./day03-input.txt")
	if err != nil {
		panic(err)
	}
	wiresCoords := parseInput(in)

	fmt.Println(PartOne(wiresCoords))
	fmt.Println(PartTwo(wiresCoords))
}

func parseInput(f io.Reader) [][]string {
	in, err := ioutil.ReadAll(f)
	if err != nil {
		log.Fatal(err)
	}

	out := strings.Split(strings.TrimSpace(string(in)), "\n")
	wires := make([][]string, len(out))
	for i := range out {
		wires[i] = strings.Split(string(out[i]), ",")
	}
	return wires
}
