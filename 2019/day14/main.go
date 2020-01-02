package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"

	"aoc/helpers/ds/queue"
)

// ElementProps is used in the map to tell how much of each element is made
// and its ingredients
type ElementProps struct {
	yield int
	ings  []Ingredient
}

// Ingredient is the ingredient for each element, including how much of it is
// required
type Ingredient struct {
	required int
	name     string
}

// EleTotals represents the element totals
type EleTotals map[string]int

// NewTotals initializes an EleTotals map and returns it
func NewTotals() EleTotals {
	return make(EleTotals)
}

var file = flag.String("file", "ex1-31.txt", "Name of input file")
var fuel = flag.Int("fuel", 1, "Num of fuel")

func main() {
	flag.Parse()
	list := parseFile(*file)

	// Part One
	//totals := NewTotals()
	//totals.getTotals(list, "FUEL", *fuel)
	//fmt.Println("Part one:", totals["ORE"])

	fmt.Println(PartTwo(list, 1e12))
}

func (t EleTotals) getTotals(list map[string]ElementProps, ele string, amount int) {
	t[ele] = amount
	q := queue.NewQueue()
	q.Put(ele)

	for q.Len() > 0 {
		i, _ := q.Get()
		ele = i.(string)
		ings, yield := list[ele].ings, list[ele].yield

		for t[ele] > 0 {
			for i := range ings {
				t[ings[i].name] += ings[i].required

				if ings[i].name != "ORE" {
					q.Put(ings[i].name)
				}
			}
			t[ele] -= yield
		}
	}
}

func parseFile(f string) map[string]ElementProps {
	in, err := ioutil.ReadFile(*file)
	if err != nil {
		panic(err)
	}
	out := string(in[:len(in)-1])

	list := make(map[string]ElementProps)
	reLine := regexp.MustCompile(`(\d+ \w+.*) => (.+)`)
	reEle := regexp.MustCompile(`(\d+) (\w+)`)
	for _, line := range strings.Split(out, "\n") {
		var ings []Ingredient
		found := reLine.FindStringSubmatch(line)
		ele := reEle.FindStringSubmatch(found[2])
		eleReq, err := strconv.Atoi(ele[1])
		if err != nil {
			panic(err)
		}

		splitIngs := strings.Split(found[1], ", ")
		for _, d := range splitIngs {
			e := reEle.FindStringSubmatch(d)
			req, err := strconv.Atoi(e[1])
			if err != nil {
				panic(err)
			}
			ings = append(ings, Ingredient{required: req, name: e[2]})
		}

		list[ele[2]] = ElementProps{yield: eleReq, ings: ings}
	}
	return list
}
