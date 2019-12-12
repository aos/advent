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
	onComma := func(data []byte, atEOF bool) (int, []byte, error) {
		for i := 0; i < len(data); i++ {
			if data[i] == ',' {
				return i + 1, data[:i], nil
			}
		}

		return 0, data, bufio.ErrFinalToken
	}
	scanner.Split(onComma)

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
