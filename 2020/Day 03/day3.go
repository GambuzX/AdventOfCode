package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func getCoordsInBounds(lines []string, x, y int) (int, int) {
	return x % len(lines[0]), y % len(lines)
}

func treeCount(lines []string, slopeX, slopeY int) (total int) {
	total = 0
	x, y := 0, 0

	for y < len(lines) {
		mapX, mapY := getCoordsInBounds(lines, x, y)
		if lines[mapY][mapX] == '#' {
			total++
		}

		x += slopeX
		y += slopeY
	}

	return
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	lines := strings.Split(content, "\n")

	fmt.Println("Part 1: %d", treeCount(lines, 3, 1))

	mult := treeCount(lines, 1, 1) * treeCount(lines, 3, 1) * treeCount(lines, 5, 1) * treeCount(lines, 7, 1) * treeCount(lines, 1, 2)
	fmt.Println("Part 2: %d", mult)
}
