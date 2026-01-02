package main

import (
	"testing"
)

type Book struct {
	Title string
	Author string
	Year int
	Genre string
}

func NewBook(title string, author string, year int, genre string) *Book {
	return &Book{Title: title, Author: author, Year: year, Genre: genre}
}

func TestNewBook(t *testing.T) {
	book := NewBook("Тестовая книга", "Тестовый автор", 2022, "Тестовый жанр")

	if book.Title != "Тестовая книга" {
		t.Errorf("Ожидается название 'Тестовая книга', получено '%s'", book.Title)
	}

	if book.Author != "Тестовый автор" {
		t.Errorf("Ожидается автор 'Тестовый автор', получено '%s'", book.Author)
	}

	if book.Year != 2022 {
		t.Errorf("Ожидается год выпуска 2022, получено %d", book.Year)
	}

	if book.Genre != "Тестовый жанр" {
		t.Errorf("Ожидается жанр 'Тестовый жанр', получено '%s'", book.Genre)
	}
}