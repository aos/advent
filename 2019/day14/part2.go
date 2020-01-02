// Part 2
package main

func (t EleTotals) returnOre() int {
	ore := t["ORE"]
	t["ORE"] = 0
	return ore
}

func (t EleTotals) isInitial() bool {
	for _, v := range t {
		if v != 0 {
			return false
		}
	}
	return true
}

// PartTwo ...
func PartTwo(list map[string]ElementProps, ore int) int {
	t := NewTotals()
	initialOre := ore
	fuel := 0

	for ore > 0 {
		t.getTotals(list, "FUEL", 1)

		fuel++
		ore -= t.returnOre()
		if t.isInitial() {
			break
		}
	}
	return (fuel * initialOre) / (initialOre - ore)
}
