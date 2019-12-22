// Day 8
package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
)

func main() {
	var image [][]int
	layerSize := 25 * 6
	nums := parseFile("./day08-input.txt")

	var layer []int
	lastZeroesCount := math.MaxInt32
	numZeroes := 0
	zeroesLayer := 0
	for i, n := range nums {
		if n == 0 {
			numZeroes++
		}
		layer = append(layer, n)

		if (i+1)%layerSize == 0 {
			image = append(image, layer)
			layer = nil

			if numZeroes < lastZeroesCount {
				zeroesLayer = len(image) - 1
				lastZeroesCount = numZeroes
			}

			numZeroes = 0
		}
	}
	fmt.Println(multiplyDigits(image[zeroesLayer]))
}

func multiplyDigits(layer []int) int {
	onesCount := 0
	twosCount := 0

	for _, n := range layer {
		if n == 1 {
			onesCount++
		}
		if n == 2 {
			twosCount++
		}
	}

	return onesCount * twosCount
}

func parseFile(f string) []int {
	out, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	out = out[:len(out)-1]
	ints := make([]int, len(out))

	for i := range out {
		num, err := strconv.Atoi(string(out[i]))
		if err != nil {
			panic(err)
		}
		ints[i] = num
	}
	return ints
}
