package main

import (
	"math"
	"fmt"
)

type Shape interface {
	Area() float64
}

type Circle struct {
	radius float64
}

type Rectangle struct {
	width float64
	height float64
}

func (c Circle) Area() float64 {
	return math.Pi * (math.Pow(c.radius, 2))
}

func (r Rectangle) Area() float64 {
	return r.width * r.height
}

func main() {
	figure_1 := Circle{radius: 1.0}
	fmt.Println(figure_1.Area())
	figure_2 := Rectangle{width: 57.2, height: 10.2}
	fmt.Println(figure_2.Area())
}