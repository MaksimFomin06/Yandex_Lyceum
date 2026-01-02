package main

import "fmt"

type User struct {
	Name string
	Age int
	IsActive bool
}

func NewUser(name string, age int) (*User, error) {
	defaultAge := 18
	defaultStatus := true
	if name == "" {
		return nil, fmt.Errorf("name is empty for user")
	} else if age <= 0 {
		age = defaultAge
	}

	return &User{Name: name, Age: age, IsActive: defaultStatus}, nil
}