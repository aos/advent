// Day 8
package main

import (
	"fmt"
	"io/ioutil"
	"math"
)

func main() {
	var image [][]byte
	layerSize := 2 * 2
	nums := parseFile("./day08-example2.txt")

	var layer []byte
	lastZeroesCount := math.MaxInt32
	numZeroes := 0
	zeroesLayer := 0
	for i, n := range nums {
		if n == '0' {
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
	fmt.Println("Part 1:", multiplyDigits(image[zeroesLayer]))
}

// Part 1
func multiplyDigits(layer []byte) int {
	onesCount := 0
	twosCount := 0

	for _, n := range layer {
		if n == '1' {
			onesCount++
		}
		if n == '2' {
			twosCount++
		}
	}

	return onesCount * twosCount
}

func renderImage([][]byte) {

}

func parseFile(f string) []byte {
	out, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	return out[:len(out)-1]
}
