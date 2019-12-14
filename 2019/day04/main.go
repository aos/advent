// Day 4
// Input:
// 248345-746315
package main

import "fmt"

func main() {
	fmt.Println(checkCriteria(248345, 746315, PartOne))
	fmt.Println(checkCriteria(248345, 746315, PartTwo))
}

func checkCriteria(min, max int, f func(n int) bool) int {
	meetsCriteria := 0
	for n := min; n < max+1; n++ {
		if res := f(n); res {
			meetsCriteria++
		}
	}
	return meetsCriteria
}
