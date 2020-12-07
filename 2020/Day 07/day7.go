package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type bagAmount struct {
	color  string
	amount int
}

func find(curr string, rules map[string][]bagAmount) bool {
	if curr == target {
		return true
	}

	amounts := rules[curr]
	for _, amount := range amounts {
		if find(amount.color, rules) {
			return true
		}
	}
	return false
}

func countRecursive(curr string, rules map[string][]bagAmount) int {
	total := 0
	amounts := rules[curr]
	for _, amount := range amounts {
		total += amount.amount + amount.amount*countRecursive(amount.color, rules)
	}
	return total
}

func part1(rules map[string][]bagAmount) {
	total := 0
	for color := range rules {
		if find(color, rules) {
			total++
		}
	}
	total-- // do not consider shiny gold bag
	fmt.Printf("Part 1: %d\n", total)
}

func part2(rules map[string][]bagAmount) {
	total := countRecursive(target, rules)
	fmt.Printf("Part 2: %d\n", total)
}

var target string = "shiny gold"

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	rulesS := strings.Split(content, "\n")

	rules := make(map[string][]bagAmount)
	for _, rule := range rulesS {
		var re = regexp.MustCompile(`(?m)(.*)\sbags\scontain`)
		colour := re.FindAllStringSubmatch(rule, -1)[0][1]

		re = regexp.MustCompile(`(?m)(\d)\s([a-z\s]*)\sbag(?:s?(?:,|\.))`)
		for _, match := range re.FindAllStringSubmatch(rule, -1) {
			amount, _ := strconv.Atoi(match[1])
			c := match[2]

			rules[colour] = append(rules[colour], bagAmount{color: c, amount: amount})
		}
	}

	part1(rules)
	part2(rules)
}
