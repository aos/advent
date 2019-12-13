// Day 2
package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"

	"aoc/helpers"
)

func main() {
	input, err := os.Open("./day02-input.txt")
	defer input.Close()
	if err != nil {
		log.Fatal(err)
	}

	opcodes := convertToOpcodes(input)

	fmt.Println("Part one:", PartOne(opcodes))
	fmt.Println("Part two:", PartTwo(opcodes))
}

func convertToOpcodes(input io.Reader) []int {
	var opcodes []int

	scanner := bufio.NewScanner(input)
	scanner.Split(helpers.SplitComma)

	for scanner.Scan() {
		t := strings.TrimSuffix(scanner.Text(), "\n")
		toInt, err := strconv.Atoi(t)
		if err != nil {
			log.Fatal(err)
		}
		opcodes = append(opcodes, toInt)
	}
	return opcodes
}
