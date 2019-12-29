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
	return fmt.Sprintf("Moon(pos=<x=%4d, y=%4d, z=%4d>, vel=<x=%4d, y=%4d, z=%4d>)\n",
		m.pos.x, m.pos.y, m.pos.z, m.vel.x, m.vel.y, m.vel.z)
}

type orbit struct {
	currentState []moon
	startState   []moon
	rounds       int
}

func (o *orbit) step() {
	for i := range o.currentState {
		x, y, z := 0, 0, 0
		for j := range o.currentState {
			if o.currentState[i] == o.currentState[j] {
				continue
			}
			if o.currentState[i].pos.x > o.currentState[j].pos.x {
				x--
			} else if o.currentState[i].pos.x < o.currentState[j].pos.x {
				x++
			}
			if o.currentState[i].pos.y > o.currentState[j].pos.y {
				y--
			} else if o.currentState[i].pos.y < o.currentState[j].pos.y {
				y++
			}
			if o.currentState[i].pos.z > o.currentState[j].pos.z {
				z--
			} else if o.currentState[i].pos.z < o.currentState[j].pos.z {
				z++
			}
		}
		o.currentState[i].vel.x += x
		o.currentState[i].vel.y += y
		o.currentState[i].vel.z += z
	}
	for i := range o.currentState {
		o.currentState[i].pos.x += o.currentState[i].vel.x
		o.currentState[i].pos.y += o.currentState[i].vel.y
		o.currentState[i].pos.z += o.currentState[i].vel.z
	}
}

func (o orbit) String() string {
	var sb strings.Builder
	for _, s := range o.currentState {
		sb.WriteString(s.String())
	}
	return sb.String()
}

var debug = flag.Bool("debug", false, "Print debug info")
var part = flag.Int("part", 1, "Which part to run?")
var rounds = flag.Int("rounds", 1000, "How many rounds to run")

func main() {
	flag.Parse()
	moons := parseFile("./day12-input.txt")
	start := make([]moon, len(moons))
	copy(start, moons)

	orbit := orbit{
		currentState: moons,
		startState:   start,
	}
	stateMap := make(map[string]bool)
	cycles := make([]int, 3)

	numFound := 0
	// Steps
	for {
		if *part == 1 && *debug {
			fmt.Printf("After %d steps:\n", orbit.rounds)
		}
		if *part == 1 && orbit.rounds == *rounds {
			break
		}

		if *part == 2 {
			stateX := stateAxisX(orbit.currentState)
			stateY := stateAxisY(orbit.currentState)
			stateZ := stateAxisZ(orbit.currentState)
			if !stateMap[stateX] {
				stateMap[stateX] = true
			} else if cycles[0] == 0 {
				numFound++
				cycles[0] = orbit.rounds
			}
			if !stateMap[stateY] {
				stateMap[stateY] = true
			} else if cycles[1] == 0 {
				numFound++
				cycles[1] = orbit.rounds
			}
			if !stateMap[stateZ] {
				stateMap[stateZ] = true
			} else if cycles[2] == 0 {
				numFound++
				cycles[2] = orbit.rounds
			}

			if numFound == 3 {
				fmt.Println(h.LCM(cycles[0], cycles[1], cycles[2]))
				break
			}
		}

		orbit.step()
		orbit.rounds++
	}

	if *part == 1 {
		total := 0
		for i := range orbit.currentState {
			pot := h.Abs(orbit.currentState[i].pos.x) + h.Abs(orbit.currentState[i].pos.y) + h.Abs(orbit.currentState[i].pos.z)
			kin := h.Abs(orbit.currentState[i].vel.x) + h.Abs(orbit.currentState[i].vel.y) + h.Abs(orbit.currentState[i].vel.z)
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

func stateAxisX(state []moon) string {
	var sb strings.Builder
	for i := range state {
		s := fmt.Sprintf("X(pos=%d,vel=%d)",
			state[i].pos.x,
			state[i].vel.x)
		sb.WriteString(s)
	}
	return sb.String()
}

func stateAxisY(state []moon) string {
	var sb strings.Builder
	for i := range state {
		s := fmt.Sprintf("Y(pos=%d,vel=%d)",
			state[i].pos.y,
			state[i].vel.y)
		sb.WriteString(s)
	}
	return sb.String()
}

func stateAxisZ(state []moon) string {
	var sb strings.Builder
	for i := range state {
		s := fmt.Sprintf("Z(pos=%d,vel=%d)",
			state[i].pos.z,
			state[i].vel.z)
		sb.WriteString(s)
	}
	return sb.String()
}
