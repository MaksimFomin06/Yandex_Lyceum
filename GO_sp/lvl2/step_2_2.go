package main

import (
	"math"
)

func findDiscriminant(a, b, c float64) float64 {
	d := math.Pow(b, 2) - (4 * a * c)

	return d
}

func SquareRoots(a, b, c float64) (float64, float64) {
	d := findDiscriminant(a, b, c)

	var x1, x2 float64

	if (d > 0) {
		x1 = (-b + math.Sqrt(d))/(2 * a)
		x2 = (-b - math.Sqrt(d))/(2 * a)
	} else if (d == 0) {
		x1 = (-b + math.Sqrt(d))/(2 * a)
		x2 = x1 
	} else {
		x1 = 0
		x2 = 0
	}

	return x2, x1
}