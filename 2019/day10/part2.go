// Part 2
package main

import (
	"aoc/helpers/geo"
	"sort"
)

// PointProperties declares the point along with a distance measurement (to a
// compared point)
type PointProperties struct {
	point    geo.Point
	distance float64
}

// PartTwo ...
func PartTwo(asteroids []geo.Point, a geo.Point) int {
	quadrants := make(map[int]map[float64][]PointProperties)
	for k := range asteroids {
		if asteroids[k] == a {
			continue
		}
		dir := a.AdjacentPointDirection(asteroids[k])
		if quadrants[dir] == nil {
			quadrants[dir] = make(map[float64][]PointProperties)
		}
		s := geo.SlopeOfPoints(a, asteroids[k])
		p := PointProperties{
			point:    asteroids[k],
			distance: a.DistanceTo(asteroids[k]),
		}
		toSort := append(quadrants[dir][s], p)
		if len(toSort) > 1 {
			sort.Slice(toSort, func(i, j int) bool {
				return toSort[i].distance < toSort[j].distance
			})
		}
		quadrants[dir][s] = toSort
	}

	totalAsteroids := len(asteroids)
	numDestroyed := 0
	qIdx := 0

	for totalAsteroids > 1 {
		slopes := quadrants[qIdx]
		var keys []float64
		for i := range slopes {
			keys = append(keys, i)
		}
		sort.Float64s(keys)
		if len(keys) > 0 {
			for i := range keys {
				first := keys[i]
				x := quadrants[qIdx][first][0]
				quadrants[qIdx][first] = quadrants[qIdx][first][1:]
				totalAsteroids--
				numDestroyed++
				if numDestroyed == 200 {
					return (x.point.X * 100) + x.point.Y
				}

				if len(quadrants[qIdx][first]) == 0 {
					delete(quadrants[qIdx], first)
				}
			}
		}

		qIdx++
		if qIdx > 7 {
			qIdx = 0
		}
	}
	return -1
}
