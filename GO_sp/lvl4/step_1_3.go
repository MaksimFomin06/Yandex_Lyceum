package main

import "fmt"

type Student struct {
	name string
	solvedProblems int
	scoreForOneTask float64
	passingScore float64
}

func (s Student) IsExcellentStudent() bool {
	avg_score := float64(s.solvedProblems) * s.scoreForOneTask
	if avg_score >= s.passingScore {
		return true
	} else {
		return false
	}
}

func main() {
	student := Student{name: "Gosha", solvedProblems: 30, scoreForOneTask: 10.0, passingScore: 290.0}
	fmt.Print(student.IsExcellentStudent())
}