package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type pair struct {
	addr, val int
}

type entry struct {
	bitmask string
	updates []pair
}

func createMask(size int, ones bool, reverse map[int]bool) int {
	res := 0
	for i := 0; i < size; i++ {
		sumOne := (ones && !reverse[i]) || (!ones && reverse[i])
		if sumOne {
			res++
		}

		if i < size-1 {
			res = res << 1
		}
	}
	return res
}

func getCombinationsHelper(s string, i int, res *[]string) {
	if i == len(s) {
		*res = append(*res, s)
		return
	}

	if s[i] != 'X' {
		getCombinationsHelper(s, i+1, res)
		return
	}

	newS := s[:i] + "0" + s[i+1:]
	getCombinationsHelper(newS, i+1, res)
	newS = s[:i] + "1" + s[i+1:]
	getCombinationsHelper(newS, i+1, res)
}

func getCombinations(s string) []string {
	res := make([]string, 0, 0)
	getCombinationsHelper(s, 0, &res)
	return res
}

func applyBitmask(num int, bitmask string) int {
	res := num
	zeroes := make(map[int]bool, 0)
	ones := make(map[int]bool, 0)
	for i, c := range bitmask {
		if c == '0' {
			zeroes[i] = true
		}
		if c == '1' {
			ones[i] = true
		}
	}

	zeroMask := createMask(36, false, ones)
	onesMask := createMask(36, true, zeroes)

	return (res | zeroMask) & onesMask
}

func applyAddressBitmask(addr int, bitmask string) []int {
	binaryAddr := strconv.FormatInt(int64(addr), 2)
	binaryAddr = fmt.Sprintf("%036v", binaryAddr)

	newAddr := ""
	for i, c := range bitmask {
		if c != '0' {
			newAddr += string(c)
		} else {
			newAddr += string(binaryAddr[i])
		}
	}

	options := getCombinations(newAddr)
	res := make([]int, len(options))
	for i, option := range options {
		v, _ := strconv.ParseInt(option, 2, 64)
		res[i] = int(v)
	}
	return res
}

func part1(entries []entry) {
	memory := make(map[int]int)

	for _, entry := range entries {
		for _, update := range entry.updates {
			memory[update.addr] = applyBitmask(update.val, entry.bitmask)
		}
	}

	total := 0
	for key := range memory {
		total += memory[key]
	}
	fmt.Printf("Part 1: %d\n", total)
}

func part2(entries []entry) {
	memory := make(map[int]int)

	for _, entry := range entries {
		for _, update := range entry.updates {
			addresses := applyAddressBitmask(update.addr, entry.bitmask)
			for _, addr := range addresses {
				memory[addr] = update.val
			}
		}
	}

	total := 0
	for key := range memory {
		total += memory[key]
	}
	fmt.Printf("Part 2: %d\n", total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	masks := strings.Split(content, "mask = ")
	masks = masks[1:] // first is empty

	entries := make([]entry, 0)
	var re = regexp.MustCompile(`(?m)mem\[(\d*)\]\s=\s(\d*)`)
	for _, mask := range masks {
		bitmask := strings.Split(mask, "\n")[0]

		updates := make([]pair, 0)
		for _, match := range re.FindAllStringSubmatch(mask, -1) {
			addr, _ := strconv.Atoi(match[1])
			val, _ := strconv.Atoi(match[2])
			updates = append(updates, pair{addr: addr, val: val})
		}
		entries = append(entries, entry{bitmask: bitmask, updates: updates})
	}

	part1(entries)
	part2(entries)
}
