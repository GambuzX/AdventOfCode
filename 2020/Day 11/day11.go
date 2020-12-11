package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func diagramHash(d [][]rune) string {
	final := ""
	for _, line := range d {
		final += string(line)
	}
	return final
}

func copyDiagram(d [][]rune) [][]rune {
	copyD := make([][]rune, len(d))
	for i, line := range d {
		copyD[i] = make([]rune, len(line))
		copy(copyD[i], d[i])
	}
	return copyD
}

func countAdjacentOccupied(d [][]rune, row, col int) int {
	total := 0
	positions := [][]int{
		{row - 1, col},
		{row + 1, col},
		{row, col - 1},
		{row, col + 1},
		{row - 1, col - 1},
		{row - 1, col + 1},
		{row + 1, col - 1},
		{row + 1, col + 1},
	}

	for _, pair := range positions {
		r, c := pair[0], pair[1]
		if r < 0 || c < 0 || r >= len(d) || c >= len(d[0]) {
			continue
		}
		if d[r][c] == '#' {
			total++
		}
	}

	return total
}

func countVisibleSeats(d [][]rune, row, col int) int {
	total := 0
	directions := [][]int{
		{-1, 0},
		{1, 0},
		{0, -1},
		{0, 1},
		{-1, -1},
		{-1, 1},
		{1, -1},
		{1, 1},
	}

	for _, pair := range directions {
		vert, horiz := pair[0], pair[1]
		currRow, currCol := row+vert, col+horiz

		for !(currRow < 0 || currCol < 0 || currRow >= len(d) || currCol >= len(d[0])) {
			c := d[currRow][currCol]
			if c == '#' {
				total++
				break
			}
			if c == 'L' {
				break
			}

			currRow += vert
			currCol += horiz
		}
	}

	return total
}

func updateDiagram(d [][]rune) {
	old := copyDiagram(d)
	for i, line := range old {
		for j, c := range line {
			occupied := countAdjacentOccupied(old, i, j)
			if c == 'L' && occupied == 0 {
				d[i][j] = '#'
			}

			if c == '#' && occupied >= 4 {
				d[i][j] = 'L'
			}
		}
	}
}

func updateDiagram2(d [][]rune) {
	old := copyDiagram(d)
	for i, line := range old {
		for j, c := range line {
			occupied := countVisibleSeats(old, i, j)
			if c == 'L' && occupied == 0 {
				d[i][j] = '#'
			}

			if c == '#' && occupied >= 5 {
				d[i][j] = 'L'
			}
		}
	}
}

func getOccupied(d [][]rune) int {
	total := 0
	for _, line := range d {
		for _, c := range line {
			if c == '#' {
				total++
			}
		}
	}
	return total
}

func part1(original [][]rune) {
	d := copyDiagram(original)
	seen := make(map[string]bool)
	for {
		s := diagramHash(d)
		if seen[s] {
			occupied := getOccupied(d)
			fmt.Printf("Part 1: %d\n", occupied)
			return
		}

		seen[s] = true
		updateDiagram(d)
	}
}

func part2(original [][]rune) {
	d := copyDiagram(original)
	seen := make(map[string]bool)
	for {
		s := diagramHash(d)
		if seen[s] {
			occupied := getOccupied(d)
			fmt.Printf("Part 2: %d\n", occupied)
			return
		}

		seen[s] = true
		updateDiagram2(d)
	}
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	inputS := strings.Split(content, "\n")

	diagram := make([][]rune, len(inputS))
	for i, line := range inputS {
		diagram[i] = make([]rune, len(inputS[0]))
		for j, c := range line {
			diagram[i][j] = c
		}
	}

	part1(diagram)
	part2(diagram)
}
