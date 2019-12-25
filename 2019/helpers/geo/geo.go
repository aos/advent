// Package geo adds helper functions (and Point struct) for geometry
package geo

import (
	h "aoc/helpers"
	"math"
)

// Point is an X,Y coordinate location
type Point struct {
	X int
	Y int
}

// AdjacentPointDirection retrieves the direction of a point relative to our
// current point. The return value is an integer specifying the direction:
//	7 0 1
//	6 * 2
//	5 4 3
// Note: the y-axis is assumed to increase downwards
func (p *Point) AdjacentPointDirection(other Point) int {
	if other.X > p.X {
		if other.Y > p.Y {
			return 3
		}
		if other.Y == p.Y {
			return 2
		}
		return 1
	}
	if other.X < p.X {
		if other.Y > p.Y {
			return 5
		}
		if other.Y == p.Y {
			return 6
		}
		return 7
	}
	if other.Y > p.Y {
		return 4
	}
	return 0
}

// DistanceTo calculates the distance to another Point
func (p *Point) DistanceTo(other Point) float64 {
	y := math.Pow(float64(other.Y-p.Y), 2)
	x := math.Pow(float64(other.X-p.X), 2)
	return math.Sqrt(x + y)
}

// ManhattanDistance calculates the manhattan distances between two Points
func ManhattanDistance(p1, p2 Point) int {
	return h.Abs(p1.X-p2.X) + h.Abs(p1.Y-p2.Y)
}

// SlopeOfPoints calculates the slope between two Points
func SlopeOfPoints(p1, p2 Point) float64 {
	return float64(p2.Y-p1.Y) / float64(p2.X-p1.X)
}

// CastLine casts a line between two Points, returns a list of crossing Points
// This uses Bresenham's algorithm
func CastLine(p1, p2 Point) []Point {
	var points []Point
	dX := h.Abs(p2.X - p1.X)
	dY := h.Abs(p2.Y - p1.Y)
	err := dX - dY
	x, y := p1.X, p1.Y
	sX := 1
	if p1.X > p2.X {
		sX = -1
	}
	sY := 1
	if p1.Y > p2.Y {
		sY = -1
	}
	for {
		points = append(points, Point{X: x, Y: y})
		if x == p2.X && y == p2.Y {
			break
		}

		e2 := 2 * err
		if e2 > -dY {
			err -= dY
			x += sX
		}
		if e2 < dX {
			err += dX
			y += sY
		}
	}
	return points
}
