package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type RuleType int

const (
	MatchChar RuleType = iota
	MatchRules
)

type rule struct {
	id           int
	RuleType     RuleType
	RulesToMatch [][]int
	CharToMatch  string
}

func (r rule) match(msg string, left int, rules map[int]rule) []int {
	switch r.RuleType {
	case MatchChar:
		if string(msg[left]) == r.CharToMatch {
			return []int{left + 1}
		}
		return []int{}
	case MatchRules:
		returnOptions := []int{}

		for _, option := range r.RulesToMatch { // match any of them

			currIndexes := []int{left}
			newIndexes := []int{}
			for _, nextRuleID := range option {

				nextRule := rules[nextRuleID]
				for _, l := range currIndexes {
					nextLeftOptions := nextRule.match(msg, l, rules)
					newIndexes = append(newIndexes, nextLeftOptions...)
				}

				currIndexes = newIndexes
				newIndexes = []int{}
			}

			returnOptions = append(returnOptions, currIndexes...)

		}
		return returnOptions
	}
	return []int{}
}

func (r rule) match2(msg string, left int, rules map[int]rule) []int {
	switch r.RuleType {
	case MatchChar:
		if left < len(msg) && string(msg[left]) == r.CharToMatch {
			return []int{left + 1}
		}
		return []int{}
	case MatchRules:
		returnOptions := []int{}

		for _, option := range r.RulesToMatch { // match any of them

			currIndexes := []int{left}
			newIndexes := []int{}
			for _, nextRuleID := range option {

				nextRule := rules[nextRuleID]
				for _, l := range currIndexes {
					nextLeftOptions := nextRule.match2(msg, l, rules)
					newIndexes = append(newIndexes, nextLeftOptions...)
				}

				currIndexes = newIndexes
				newIndexes = []int{}
			}

			returnOptions = append(returnOptions, currIndexes...)

		}
		return returnOptions
	}
	return []int{}
}

func part1() {
	rules, messages := parseInput("./input.txt")
	total := 0
	for _, msg := range messages {
		matches := rules[0].match(msg, 0, rules)
		for _, lastIndex := range matches {
			if lastIndex == len(msg) {
				total++
			}
		}
	}
	fmt.Printf("Part 1: %d\n", total)
}

func part2() {
	rules, messages := parseInput("./input2.txt")

	total := 0
	for _, msg := range messages {
		matches := rules[0].match2(msg, 0, rules)
		for _, lastIndex := range matches {
			if lastIndex == len(msg) {
				total++
			}
		}
	}
	fmt.Printf("Part 2: %d\n", total)
}

func parseInput(filename string) (map[int]rule, []string) {
	dat, _ := ioutil.ReadFile(filename)
	content := string(dat)

	rules := make(map[int]rule)
	re := regexp.MustCompile(`(?m)(\d+):\s([a-z"\d\|\s]+?)\n`)
	for _, match := range re.FindAllStringSubmatch(content, -1) {
		ruleNo, _ := strconv.Atoi(match[1])
		rulesString := match[2]

		var ruleType RuleType
		rulesToMatch := make([][]int, 0)
		charToMatch := ""

		if rulesString[0] == '"' {
			ruleType = MatchChar
			charToMatch = string(rulesString[1])
		} else {
			ruleType = MatchRules
			parts := strings.Split(rulesString, " | ")
			for _, part := range parts {

				toMatch := strings.Split(part, " ")
				curr := make([]int, 0)
				for _, numS := range toMatch {
					num, _ := strconv.Atoi(numS)
					curr = append(curr, num)
				}
				rulesToMatch = append(rulesToMatch, curr)
			}
		}
		rules[ruleNo] = rule{
			id:           ruleNo,
			RuleType:     ruleType,
			RulesToMatch: rulesToMatch,
			CharToMatch:  charToMatch,
		}

	}

	messages := make([]string, 0)
	re = regexp.MustCompile(`(?m)(a|b)+$`)
	for _, match := range re.FindAllStringSubmatch(content, -1) {
		messages = append(messages, match[0])
	}

	return rules, messages
}

func main() {
	part1()
	part2()
}
