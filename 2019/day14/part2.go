// Part 2
package main

// PartTwo uses gradient descent to get to the correct amount of FUEL
func PartTwo(list map[string]ElementProps, ore int) int {
	minOre := getTotals(list, 1)
	target := ore / minOre
	usedOre := getTotals(list, target)

	for {
		target += (ore-usedOre)/minOre + 1
		usedOre = getTotals(list, target)

		if usedOre > ore {
			break
		}
	}
	return target - 1
}
