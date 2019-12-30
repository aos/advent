// Part 2
package main

import (
	"aoc/helpers/opcodes"
	"image"
)

// PartTwo ...
func PartTwo(oc []int) int {
	oc[0] = 2
	in := make(chan int, 1)
	out, _ := opcodes.OpcodeVM(oc, in)

	ball := image.Point{X: -1, Y: -1}
	paddle := image.Point{X: -1, Y: -1}
	score := 0

	num := 0
	var insts [3]int
	for d := range out {
		insts[num] = d
		num = (num + 1) % 3

		if num == 0 {
			x, y, obj := insts[0], insts[1], insts[2]
			switch {
			case x == -1 && y == 0:
				score = obj
			// Ball
			case obj == 4:
				// Initialize location
				if ball.X == -1 && ball.Y == -1 {
					ball.X = x
					ball.Y = y
					in <- 0
				} else {
					dir := direction(ball.X, x)
					ball.X = x
					ball.Y = y

					if paddle.X >= ball.X && dir == 1 {
						in <- 0
					} else if paddle.X <= ball.X && dir == -1 {
						in <- 0
					} else {
						in <- dir
					}
				}

			// Paddle
			case obj == 3:
				paddle.X = x
				paddle.Y = y
			}
		}
	}
	return score
}

func direction(x0, x1 int) int {
	if x0 > x1 {
		return -1
	} else if x0 < x1 {
		return 1
	}
	return 0
}
