// Day 11
package main

import (
	"aoc/helpers/geo"
	"aoc/helpers/opcodes"
	"fmt"
	"image"
	"image/color"
	"image/png"
	"math"
	"os"
)

func main() {
	oc := opcodes.ReadOpcodesFromFile("./day11-input.txt")
	// All panels start black
	// 1 in:
	//	- 0 if black panel
	//	- 1 if white panel
	// 2 out:
	//	- color to paint panel robot is over (0 black, 1 white)
	//	- direction robot should turn (0 left, 1 right)
	// after turn, move forward 1 panel

	// Use map[Point]int (store coordinate and color under), initially 0
	fmt.Println("Part one:", len(paint(oc, 0)))

	fmt.Println("Part two:")
	painting := paint(oc, 1)
	minX, minY := math.MaxInt16, math.MaxInt16
	maxX, maxY := -1, -1

	for k := range painting {
		if k.X < minX {
			minX = k.X
		}
		if k.Y < minY {
			minY = k.Y
		}

		if k.X > maxX {
			maxX = k.X
		}
		if k.Y > maxY {
			maxY = k.Y
		}
	}

	// Draw to file
	img := image.NewRGBA(image.Rect(minX, minY, maxX+1, maxY+1))
	for k := range painting {
		x, y := k.X, k.Y
		if painting[k] == 1 {
			img.Set(x, y, color.RGBA{255, 255, 255, 255})
		} else {
			img.Set(x, y, color.RGBA{0, 0, 0, 255})
		}
	}
	f, _ := os.OpenFile("out.png", os.O_WRONLY|os.O_CREATE, 0600)
	defer f.Close()
	png.Encode(f, img)

	// Draw to terminal
	canvas := make([][]int, maxY+1)
	pixels := make([]int, (maxY+1)*(maxX+1))
	for i := range canvas {
		canvas[i], pixels = pixels[:maxX+1], pixels[maxX+1:]
	}
	for k := range painting {
		canvas[k.Y][k.X] = painting[k]
	}
	for i := range canvas {
		for j := range canvas[i] {
			if canvas[i][j] == 1 {
				fmt.Print("#")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println("")
	}
}

func paint(oc []int, start int) map[geo.Point]int {
	visits := make(map[geo.Point]int)
	in := make(chan int, 2)
	out, done := opcodes.OpcodeVM(oc, in)
	in <- start

	x, y := 0, 0
	currentDir := 0
	for {

		select {
		case <-done:
			return visits
		default:
			color := <-out
			dir := <-out

			visits[geo.Point{X: x, Y: y}] = color

			// change direction and move
			currentDir = changeDir(currentDir, dir)
			x, y = move(x, y, currentDir)

			in <- visits[geo.Point{X: x, Y: y}]
		}
	}
}

func move(x, y, dir int) (int, int) {
	switch dir {
	case 0:
		// up
		return x, y - 1
	case 1:
		// right
		return x + 1, y
	case 2:
		// down
		return x, y + 1
	case 3:
		// left
		return x - 1, y
	}
	return x, y
}

func changeDir(current, next int) int {
	if next == 0 {
		return (current + 3) % 4
	}
	return (current + 1) % 4
}
