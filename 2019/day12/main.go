// Day 12
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strings"

	h "aoc/helpers"
)

type axes struct {
	x, y, z int
}

type moon struct {
	pos axes
	vel axes
}

func (m moon) String() string {
	return fmt.Sprintf("Moon(pos=<x=%4d, y=%4d, z=%4d>, vel=<x=%4d, y=%4d, z=%4d>)",
		m.pos.x, m.pos.y, m.pos.z, m.vel.x, m.vel.y, m.vel.z)
}

var debug = flag.Bool("debug", false, "Print debug info")
var part = flag.Int("part", 1, "Which part to run?")
var rounds = flag.Int("rounds", 1000, "How many rounds to run")

func main() {
	flag.Parse()
	moons := parseFile("./day12-example.txt")
	start := make([]moon, len(moons))
	copy(start, moons)

	r := 0
	// Steps
	for {
		if *part == 1 && *debug {
			fmt.Printf("After %d steps:\n", r)
			for m := range moons {
				fmt.Println(moons[m])
			}
		}
		if *part == 1 && r == *rounds {
			break
		}

		// 1. Apply gravity
		//	- Change velocity of every pair of moon by +/- 1 for each axis
		for i := range moons {
			x, y, z := 0, 0, 0
			for j := range moons {
				if moons[i] == moons[j] {
					continue
				}
				if moons[i].pos.x > moons[j].pos.x {
					x--
				} else if moons[i].pos.x < moons[j].pos.x {
					x++
				}
				if moons[i].pos.y > moons[j].pos.y {
					y--
				} else if moons[i].pos.y < moons[j].pos.y {
					y++
				}
				if moons[i].pos.z > moons[j].pos.z {
					z--
				} else if moons[i].pos.z < moons[j].pos.z {
					z++
				}
			}
			moons[i].vel.x += x
			moons[i].vel.y += y
			moons[i].vel.z += z
		}
		// 2. Apply velocity
		//	- Change the position by the velocity calculated above
		for i := range moons {
			moons[i].pos.x += moons[i].vel.x
			moons[i].pos.y += moons[i].vel.y
			moons[i].pos.z += moons[i].vel.z
		}

		r++

		if *part == 2 {
			if *debug {
				fmt.Println("Step:", r)
			}
			if compareMoons(start, moons) {
				fmt.Printf("Part two: %d\n", r)
				break
			}
		}
	}

	// 3. Potential energy:
	//	- Sum(abs(pos_x), abs(pos_y), abs(pos_z))...)
	// 4. Kinetic energy
	//	- Sum(abs(vel_x), abs(vel_y), abs(vel_z))...)
	// 5. Total energy = potential * kinetic
	if *part == 1 {
		total := 0
		for i := range moons {
			pot := h.Abs(moons[i].pos.x) + h.Abs(moons[i].pos.y) + h.Abs(moons[i].pos.z)
			kin := h.Abs(moons[i].vel.x) + h.Abs(moons[i].vel.y) + h.Abs(moons[i].vel.z)
			total += (pot * kin)
		}
		fmt.Println("Part one:", total)
	}
}

func parseFile(f string) []moon {
	in, err := ioutil.ReadFile(f)
	if err != nil {
		panic(err)
	}
	out := strings.Split(string(in[:len(in)-1]), "\n")
	moons := make([]moon, len(out))
	for i := range out {
		var x, y, z int
		fmt.Sscanf(out[i], "<x=%d, y=%d, z=%d>", &x, &y, &z)
		moons[i] = moon{
			pos: axes{
				x: x,
				y: y,
				z: z,
			},
		}
	}
	return moons
}

// Part 2
func compareMoons(start, current []moon) bool {
	for i := range current {
		if start[i].pos.x != current[i].pos.x {
			return false
		}
		if start[i].pos.y != current[i].pos.y {
			return false
		}
		if start[i].pos.z != current[i].pos.z {
			return false
		}
		if start[i].vel.x != current[i].vel.x {
			return false
		}
		if start[i].vel.y != current[i].vel.y {
			return false
		}
		if start[i].vel.z != current[i].vel.z {
			return false
		}
	}
	return true
}
