package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func findStartingPos(s string, right int) int {
	rightParsCount := 0
	for i := right; i >= 0; i-- {
		c := s[i]
		switch c {
		case ')':
			rightParsCount++
		case '(':
			rightParsCount--
			if rightParsCount == 0 {
				return i
			}
		case '*':
		case '+':
			continue
		default:
			if rightParsCount == 0 {
				return i
			}
		}
	}
	return -1
}

func findClosingPos(s string, left int) int {
	leftParsCount := 0
	for i := left; i < len(s); i++ {
		c := s[i]
		switch c {
		case '(':
			leftParsCount++
		case ')':
			leftParsCount--
			if leftParsCount == 0 {
				return i
			}
		case '*':
		case '+':
			continue
		default:
			if leftParsCount == 0 {
				return i
			}
		}
	}
	return -1
}

func placeParenthesesAroundSums(formula string) string {
	chars := strings.Split(formula, "")
	res := ""
	openingParentheses := make(map[int]bool)
	closingParentheses := make(map[int]bool)
	for i, c := range chars {
		if c == "+" {
			openingParentheses[findStartingPos(formula, i)] = true
			closingParentheses[findClosingPos(formula, i)] = true
		}
	}

	for i, c := range chars {
		if openingParentheses[i] {
			res += "("
		}
		res += c
		if closingParentheses[i] {
			res += ")"
		}
	}
	return res
}

func evaluateFormula(formula string, left int) (int, int) { // return total, last index
	total := 0
	lastOp := '+'

	updateTotal := func(v int) {
		switch lastOp {
		case '+':
			total += v
		case '*':
			total *= v
		}
	}

	for i := left; i < len(formula); i++ {
		c := formula[i]
		switch c {
		case '(':
			subtotal, right := evaluateFormula(formula, i+1)
			updateTotal(subtotal)
			i = right
		case ')':
			return total, i
		case '+':
			lastOp = '+'
		case '*':
			lastOp = '*'
		default:
			v, _ := strconv.Atoi(string(c))
			updateTotal(v)
		}
	}

	return total, len(formula)
}

func part1(formulas []string) {
	total := 0
	for _, formula := range formulas {
		formula = strings.ReplaceAll(formula, " ", "")
		t, _ := evaluateFormula(formula, 0)
		total += t
	}
	fmt.Printf("Part 1: %d\n", total)
}

func part2(formulas []string) {
	total := 0
	for _, formula := range formulas {
		formula = strings.ReplaceAll(formula, " ", "")
		formula = placeParenthesesAroundSums(formula)
		t, _ := evaluateFormula(formula, 0)
		total += t
	}
	fmt.Printf("Part 2: %d\n", total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	formulas := strings.Split(content, "\n")

	part1(formulas)
	part2(formulas)
}
