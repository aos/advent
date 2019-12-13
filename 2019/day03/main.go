package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

// Wires contains the tracing for both wires
type Wires struct {
	first  []string
	second []string
}

func main() {
	in, err := os.Open("./day03-example159.txt")
	if err != nil {
		panic(err)
	}
	wires := parseInput(in)
	fmt.Println(wires)
}

func parseInput(f io.Reader) Wires {
	in, err := ioutil.ReadAll(f)
	if err != nil {
		log.Fatal(err)
	}

	out := strings.Split(string(in), "\n")
	return Wires{
		first:  strings.Split(strings.TrimSpace(string(out[0])), ","),
		second: strings.Split(strings.TrimSpace(string(out[1])), ","),
	}
}

func traceWireOnMap(w []string, grid *map[string]int) {
	for _, dot := range w {
		direction := dot[0]
		length, err := strconv.Atoi(dot[1:])
		if err != nil {
			panic(err)
		}

		switch direction {
		case 'U':
		case 'D':
		case 'L':
		case 'R':
		default:
			log.Fatal("Invalid direction", direction)
		}
	}
}
