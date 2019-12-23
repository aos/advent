// Day 8
package main

import (
	"fmt"
	"io/ioutil"
	"math"
)

func main() {
	var image [][][]byte
	width := 2
	height := 2
	layerSize := width * height
	nums := parseFile("./day08-example2.txt")

	var layer [][]byte
	var row []byte
	lastZeroesCount := math.MaxInt32
	numZeroes := 0
	zeroesLayer := 0
	for i, n := range nums {
		if n == '0' {
			numZeroes++
		}

		row = append(row, n)
		if (i+1)%width == 0 {
			layer = append(layer, row)
			row = nil
		}

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
	// fmt.Println(multiplyDigits(image[zeroesLayer]))

	fmt.Println(zeroesLayer)
	// fmt.Println(image)
	renderImage(image)
}

// Part 1
func multiplyDigits(layer [][]byte) int {
	onesCount := 0
	twosCount := 0

	for i := range layer {
		for _, n := range layer[i] {
			if n == '1' {
				onesCount++
			}
			if n == '2' {
				twosCount++
			}
		}
	}

	return onesCount * twosCount
}

// Part 2
func renderImage(image [][][]byte) {
	width := 2
	height := 2
	numLayers := len(image)
	// var final [][]byte

	for i := 0; i < width; i++ {
		for j := 0; j < height; j++ {
			var row []byte
			for l := 0; l < numLayers; l++ {
				row = append(row, image[l][j][i])
			}
		}
	}
}

func parseFile(f string) []byte {
	out, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	return out[:len(out)-1]
}
