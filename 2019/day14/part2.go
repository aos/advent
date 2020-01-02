package main

import "fmt"

func (t EleTotals) returnOre() int {
	ore := t["ORE"]
	t["ORE"] = 0
	return ore
}

// PartTwo ...
func PartTwo(list map[string]ElementProps, ore int) int {
	t := NewTotals()
	fuel := 0

	for ore > 0 {
		fmt.Println("Ore remaining:", ore)
		fuel++
		t.getTotals(list, "FUEL", 1)
		ore -= t.returnOre()
	}
	return fuel
}
