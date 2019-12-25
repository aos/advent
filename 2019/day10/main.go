package main

import (
	"aoc/helpers/geo"
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	asteroids := parseFile("./day10-input.txt")
	a, num := PartOne(asteroids)
	fmt.Println("Part one:", num)
	fmt.Println("Part two:", PartTwo(asteroids, a))
}

func parseFile(f string) []geo.Point {
	var asteroids []geo.Point
	in, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}

	out := strings.Split(string(in[:len(in)-1]), "\n")
	for i := range out {
		for j := range out[i] {
			if out[i][j] == '#' {
				asteroids = append(asteroids, geo.Point{X: j, Y: i})
			}
		}
	}
	return asteroids
}
