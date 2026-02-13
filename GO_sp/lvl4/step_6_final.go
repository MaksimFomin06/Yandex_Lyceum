package main

import (
	"fmt"
)

type Animal interface {
	MakeSound() string
	GetName() string
	GetInfo() string
}

type animal struct {
	name string
	species string
	age int
	sound string
}

type ZooKeeper struct{}

func NewAnimal(
	name string,
	species string,
	age int,
	sound string,
) Animal {
	return &animal{
		name: name,
		species: species,
		age: age,
		sound: sound,
	}
}

func (a *animal) MakeSound() string {
	return a.sound
}

func (a *animal) GetName() string {
	return a.name
}

func (a *animal) GetInfo() string {
	var output = fmt.Sprintf("Имя: %s, Вид: %s, Возраст: %d", a.name, a.species, a.age)

	return output
}

func ZooShow(animals []Animal) {
	for _, animal := range animals {
		animalInfo := animal.GetInfo()
		animalSound := animal.MakeSound()
		
		fmt.Println(animalInfo)
		fmt.Println(animalSound)
	}

}

func (zk ZooKeeper) Feed(animal Animal) {
	fmt.Printf("Смотритель зоопарка кормит %s. %s!\n", animal.GetName(), animal.MakeSound())
}