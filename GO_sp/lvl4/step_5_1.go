package main

import "fmt"

type Account struct {
	balance float64
	owner string
}

func NewAccount(owner string) *Account {
	return &Account{balance: 0.0, owner: owner}
}

func (a *Account) SetBalance(value float64) error {
	if value < 0 {
		return fmt.Errorf("Некорректное значение")
	}
	
	a.balance = value
	return nil
}

func (a *Account) GetBalance() float64 {
	return a.balance
}

func (a *Account) Deposit(value float64) error {
	if value < 0 {
		return fmt.Errorf("Некорректное значение")
	}
	newBalance := a.balance + value
	if newBalance < 0 {
		return fmt.Errorf("Баланс меньше нуля")
	}
	a.balance = newBalance
	return nil
}

func (a *Account) Withdraw(value float64) error {
	if value < 0 {
		return fmt.Errorf("Некорректное значение")
	}
	newBalance := a.balance - value
	if newBalance < 0 {
		return fmt.Errorf("Баланс меньше нуля")
	}
	a.balance = newBalance
	return nil
}