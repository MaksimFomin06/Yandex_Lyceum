package main

import "fmt"

type Person struct {
	name string
	age int
	address string
}

func (p Person) PrettyPrint() {
	fmt.Printf("Name: %s\n", p.name)
	fmt.Printf("Age: %d\n", p.age)
	fmt.Printf("Address: %s", p.address)
}

func main() {
	p1 := Person{name: "p", age: 12, address: "sd"}
	p1.PrettyPrint()
}