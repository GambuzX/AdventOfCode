package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func part1(answers []string) {
	total := 0
	for _, answer := range answers {
		seen := make(map[rune]bool)
		lines := strings.Split(answer, "\n")
		for _, line := range lines {
			for _, c := range line {
				seen[c] = true
			}
		}
		total += len(seen)
	}
	fmt.Println(total)
}

func part2(answers []string) {
	total := 0
	for _, answer := range answers {
		seen := make(map[rune]int)
		lines := strings.Split(answer, "\n")
		for _, line := range lines {
			for _, c := range line {
				seen[c]++
			}
		}

		for _, val := range seen {
			if val == len(lines) {
				total++
			}
		}
	}
	fmt.Println(total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	answers := strings.Split(content, "\n\n")

	part1(answers)
	part2(answers)
}
