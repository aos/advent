package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	input, err := os.Open("./day01-input.txt")
	defer input.Close()

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part one:", PartOne(input))

	input.Seek(0, 0)

	fmt.Println("Part two:", PartTwo(input))
}
