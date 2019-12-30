// Part 2
package main

import (
	"aoc/helpers/opcodes"
	"fmt"
	"image"
)

// PartTwo ...
func PartTwo(oc []int) int {
	oc[0] = 2

	in := make(chan int, 1)
	out, _ := opcodes.OpcodeVM(oc, in)

	ball := image.Point{}
	paddle := image.Point{}
	num := 0
	var insts [3]int
	score := 0
	for {
		select {
		case d := <-out:
			insts[num] = d
			num = (num + 1) % 3

			if num == 0 {
				switch {
				case insts[0] == -1 && insts[1] == 0:
					score = insts[2]
					fmt.Println("Score:", score)

				// Ball
				case insts[2] == 4:
					ball.X = insts[0]
					ball.Y = insts[1]

				// Paddle
				case insts[2] == 3:
					paddle.X = insts[0]
					paddle.Y = insts[1]
				}
			}
		default:
			//if ball.X > paddle.X {
			//	in <- 1 // Move paddle right
			//} else if ball.X < paddle.X {
			//	in <- -1 // Left
			//} else {
			//	in <- 0 // Stay neutral
			//}

			fmt.Println("Paddle:", paddle)
			fmt.Println("Ball:", ball)
		}
	}
}
