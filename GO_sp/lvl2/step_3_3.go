package main

import "errors"

var Balance float64 = 0

var (
	AmountIsIncorrectError = errors.New("amount is incorrect")
	BalanceIsIncorrectError = errors.New("balance is incorrect")
)

func topUpBalance(amount float64) error {
	if amount <= 0 {
		return AmountIsIncorrectError
	}
	Balance += amount
	return nil
}

func chargeFromBalance(amount float64) error {
	if amount <= 0 {
		return AmountIsIncorrectError
	}
	Balance -= amount
	if Balance < 0 {
		return BalanceIsIncorrectError
	}
	return nil
}

func TopUpAndGetBalance(amount float64) (float64, error) {
	if amount <= 0 {
		return 0, AmountIsIncorrectError
	}
	Balance += amount
	return Balance, nil
}

func ChargeFromAndGetBalance(amount float64) (float64, error) {
	if amount <= 0 {
		return 0, AmountIsIncorrectError
	}
	if amount > Balance {
		return 0, BalanceIsIncorrectError
	}
	Balance -= amount
	return Balance, nil
}