// Day 8
package main

import (
	"fmt"
	"io/ioutil"
	"math"
)

func main() {
	width := 25
	height := 6
	nums := parseFile("./day08-input.txt")

	var image [][][]byte
	var layer [][]byte
	var row []byte
	// Part 1 stuff
	lastZeroesCount := math.MaxInt16
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

		if (i+1)%(width*height) == 0 {
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

	fmt.Println("Part 2:")
	img := createImage(image, width, height)
	renderImage(img)
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
func createImage(image [][][]byte, width, height int) [][]byte {
	numLayers := len(image)
	final := make([][]byte, height)
	for i := range final {
		final[i] = make([]byte, width)
	}

	for w := 0; w < width; w++ {
		for h := 0; h < height; h++ {
			for l := 0; l < numLayers; l++ {
				if image[l][h][w] == '2' {
					continue
				}

				final[h][w] = image[l][h][w]
				break
			}
		}
	}
	return final
}

// Part 2
func renderImage(img [][]byte) {
	for i := range img {
		for j := range img[i] {
			if img[i][j] == '0' {
				fmt.Print(" ")
			} else {
				fmt.Printf("%s", string(img[i][j]))
			}
		}
		fmt.Println("")
	}
}

func parseFile(f string) []byte {
	out, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	return out[:len(out)-1]
}
