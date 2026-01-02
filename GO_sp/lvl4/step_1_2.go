package main

import "fmt"

type Employee struct {
	name string
	position string
	salary float64
	bonus float64
}

func (e Employee) CalculateTotalSalary() {
	total_salary := e.salary + e.bonus

	fmt.Printf("Employee: %s\n", e.name)
	fmt.Printf("Position: %s\n", e.position)
	fmt.Printf("Total Salary: %.2f", total_salary)
}

func main() {
	student_employee := Employee{name: "test", position: "tester", salary: 1000, bonus: 12}
	student_employee.CalculateTotalSalary()
}