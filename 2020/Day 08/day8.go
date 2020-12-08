package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type instruction struct {
	name  string
	value int
}

// returns (acc value, isFinished)
func runProgram(instructions []instruction) (int, bool) {
	acc := 0
	i := 0
	seen := make(map[int]bool)
	for {
		if i >= len(instructions) {
			return acc, true // finished
		}

		seenVal := seen[i]
		if seenVal {
			return acc, false // infinite loop
		}
		seen[i] = true

		curr := instructions[i]
		switch curr.name {
		case "acc":
			acc += curr.value
		case "jmp":
			i += curr.value - 1
		case "nop":
		}
		i++
	}
}

func switchJmpNop(instructions []instruction, i int) {
	instr := instructions[i]
	switch instr.name {
	case "nop":
		instructions[i].name = "jmp"
	case "jmp":
		instructions[i].name = "nop"
	}
}

func part1(instructions []instruction) {
	acc, _ := runProgram(instructions)
	fmt.Printf("Part 1: %d\n", acc)
}

func part2(instructions []instruction) {
	for i, instr := range instructions {
		if instr.name == "acc" {
			continue
		}

		switchJmpNop(instructions, i)
		acc, finished := runProgram(instructions)
		switchJmpNop(instructions, i)

		if finished {
			fmt.Printf("Part 2: %d\n", acc)
			return
		}

	}
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	instructionsS := strings.Split(content, "\n")

	instructions := make([]instruction, len(instructionsS), len(instructionsS))
	for i, ins := range instructionsS {
		instr := ins[:3]
		val := ins[4:]
		value, _ := strconv.Atoi(val)
		instructions[i] = instruction{
			name:  instr,
			value: value,
		}
	}

	part1(instructions)
	part2(instructions)
}
