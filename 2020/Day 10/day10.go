package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func part1(adapters []int) {
	diffs := make([]int, 4, 4)
	for i := 0; i < len(adapters)-1; i++ {
		diff := adapters[i+1] - adapters[i]
		diffs[diff]++
	}
	fmt.Printf("Part 1: %d\n", diffs[1]*diffs[3])
}

func part2(adapters []int) {
	ranges := make([]uint64, len(adapters), len(adapters))
	ranges[len(adapters)-1] = 1
	for i := len(adapters) - 2; i >= 0; i-- {
		var options uint64 = 0
		if i+1 < len(adapters) && (adapters[i+1]-adapters[i] <= 3) {
			options += ranges[i+1]
		}
		if i+2 < len(adapters) && (adapters[i+2]-adapters[i] <= 3) {
			options += ranges[i+2]
		}
		if i+3 < len(adapters) && (adapters[i+3]-adapters[i] <= 3) {
			options += ranges[i+3]
		}
		ranges[i] = options
	}
	fmt.Printf("Part 2: %d\n", ranges[0])
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	adaptersS := strings.Split(content, "\n")

	adapters := make([]int, len(adaptersS)+1, len(adaptersS)+1) // adapters[0] = 0
	for i, s := range adaptersS {
		num, _ := strconv.Atoi(s)
		adapters[i+1] = num
	}
	sort.Ints(adapters)
	adapters = append(adapters, adapters[len(adapters)-1]+3)

	part1(adapters)
	part2(adapters)
}
