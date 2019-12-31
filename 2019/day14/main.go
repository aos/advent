package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

// ElementProps is used in the map to tell how much of each element is made
// and the ingredients
type ElementProps struct {
	makes int
	deps  []Dep
}

// Dep is the dependency for each element, including how much of it requires
type Dep struct {
	requires int
	name     string
}

var file = flag.String("f", "ex1-31.txt", "Name of input file")

func main() {
	flag.Parse()
	list := parseFile(*file)
	total := make(map[string]int)

	getTotals("FUEL", 1, list, total)
	fmt.Println(total)

	totalOre := 0
	for k, v := range total {
		dep, ore := list[k], list[k].deps[0].requires
		for i := v; i > 0; i -= dep.makes {
			totalOre += ore
		}
	}
	fmt.Println(totalOre)
}

func getTotals(ele string, req int, list map[string]ElementProps, total map[string]int) {
	fmt.Printf("ele: %s, requested: %d\n", ele, req)
	deps, makes := list[ele].deps, list[ele].makes

	for i := range deps {
		depName, depReq := deps[i].name, deps[i].requires
		amount := 0
		for i := req; i > 0; i -= makes {
			amount += depReq
		}

		if d := list[depName].deps; len(d) == 1 && d[0].name == "ORE" {
			fmt.Printf("ele: %s, req: %d, dep: %s, amount: %d\n",
				ele, req, depName, amount)
			total[depName] += amount
		} else {
			getTotals(depName, amount, list, total)
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
		var deps []Dep
		found := reLine.FindStringSubmatch(line)
		ele := reEle.FindStringSubmatch(found[2])
		eleReq, err := strconv.Atoi(ele[1])
		if err != nil {
			panic(err)
		}

		splitDeps := strings.Split(found[1], ", ")
		for _, d := range splitDeps {
			e := reEle.FindStringSubmatch(d)
			req, err := strconv.Atoi(e[1])
			if err != nil {
				panic(err)
			}
			deps = append(deps, Dep{requires: req, name: e[2]})
		}

		list[ele[2]] = ElementProps{makes: eleReq, deps: deps}
	}
	return list
}
