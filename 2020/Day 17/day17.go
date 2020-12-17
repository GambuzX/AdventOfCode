package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type point struct {
	x, y, z int
}
type change struct {
	Coord point
	val   rune
}

type point2 struct {
	x, y, z, w int
}
type change2 struct {
	Coord point2
	val   rune
}

func isInDiagram(z, y, x int, d map[int]map[int]map[int]rune) bool {
	if _, ok := d[z]; !ok {
		return false
	}
	if _, ok := d[z][y]; !ok {
		return false
	}

	_, ok := d[z][y][x]
	return ok
}

func isInDiagram2(w, z, y, x int, d map[int]map[int]map[int]map[int]rune) bool {
	if _, ok := d[w]; !ok {
		return false
	}
	if _, ok := d[w][z]; !ok {
		return false
	}
	if _, ok := d[w][z][y]; !ok {
		return false
	}

	_, ok := d[w][z][y][x]
	return ok
}

func safeInsertRune(val rune, z, y, x int, d map[int]map[int]map[int]rune) {

	if _, ok := d[z]; !ok {
		d[z] = make(map[int]map[int]rune)
	}
	if _, ok := d[z][y]; !ok {
		d[z][y] = make(map[int]rune)
	}

	d[z][y][x] = val
}

func safeInsertRune2(val rune, w, z, y, x int, d map[int]map[int]map[int]map[int]rune) {

	if _, ok := d[w]; !ok {
		d[w] = make(map[int]map[int]map[int]rune)
	}
	if _, ok := d[w][z]; !ok {
		d[w][z] = make(map[int]map[int]rune)
	}
	if _, ok := d[w][z][y]; !ok {
		d[w][z][y] = make(map[int]rune)
	}

	d[w][z][y][x] = val
}

func safeIncrement(z, y, x int, d map[int]map[int]map[int]int) {

	if _, ok := d[z]; !ok {
		d[z] = make(map[int]map[int]int)
	}
	if _, ok := d[z][y]; !ok {
		d[z][y] = make(map[int]int)
	}

	d[z][y][x]++
}

func safeIncrement2(w, z, y, x int, d map[int]map[int]map[int]map[int]int) {

	if _, ok := d[w]; !ok {
		d[w] = make(map[int]map[int]map[int]int)
	}
	if _, ok := d[w][z]; !ok {
		d[w][z] = make(map[int]map[int]int)
	}
	if _, ok := d[w][z][y]; !ok {
		d[w][z][y] = make(map[int]int)
	}

	d[w][z][y][x]++
}

func getNeighbours(x, y, z int) []point {
	increments := []int{-1, 0, 1}
	points := make([]point, 0)
	for _, zinc := range increments {
		newZ := z + zinc
		for _, yinc := range increments {
			newY := y + yinc
			for _, xinc := range increments {
				newX := x + xinc
				if !(zinc == 0 && yinc == 0 && xinc == 0) {
					points = append(points, point{x: newX, y: newY, z: newZ})
				}
			}
		}
	}
	return points
}

func getNeighbours2(x, y, z, w int) []point2 {
	increments := []int{-1, 0, 1}
	points := make([]point2, 0)
	for _, winc := range increments {
		newW := w + winc
		for _, zinc := range increments {
			newZ := z + zinc
			for _, yinc := range increments {
				newY := y + yinc
				for _, xinc := range increments {
					newX := x + xinc
					if !(winc == 0 && zinc == 0 && yinc == 0 && xinc == 0) {
						points = append(points, point2{w: newW, x: newX, y: newY, z: newZ})
					}
				}
			}
		}
	}
	return points
}

func step(diagram *map[int]map[int]map[int]rune) {

	changes := make([]change, 0)
	reverseNeighboursActiveCount := make(map[int]map[int]map[int]int)
	for z, matrix := range *diagram {
		for y, line := range matrix {
			for x, c := range line {

				// count active neighbours
				activeNeighbours := 0
				neighbours := getNeighbours(x, y, z)
				for _, n := range neighbours {
					found, ok := (*diagram)[n.z][n.y][n.x]
					if ok && found == '#' {
						activeNeighbours++
					}

					// check if neighbour is not on current diagram
					if c == '#' && !isInDiagram(n.z, n.y, n.x, *diagram) {
						safeIncrement(n.z, n.y, n.x, reverseNeighboursActiveCount)
					}
				}

				// register changes
				if c == '#' && !(activeNeighbours == 2 || activeNeighbours == 3) {
					changes = append(changes, change{
						Coord: point{x: x, y: y, z: z},
						val:   '.',
					})
				} else if c == '.' && activeNeighbours == 3 {
					changes = append(changes, change{
						Coord: point{x: x, y: y, z: z},
						val:   '#',
					})
				}

			}
		}
	}
	for z, matrix := range reverseNeighboursActiveCount {
		for y, line := range matrix {
			for x, count := range line {
				if count == 3 {
					changes = append(changes, change{
						Coord: point{x: x, y: y, z: z},
						val:   '#',
					})
				}
			}
		}
	}

	// apply changes
	for _, c := range changes {
		safeInsertRune(c.val, c.Coord.z, c.Coord.y, c.Coord.x, *diagram)
	}
}

func step2(diagram *map[int]map[int]map[int]map[int]rune) {

	changes := make([]change2, 0)
	reverseNeighboursActiveCount := make(map[int]map[int]map[int]map[int]int)
	for w, smt := range *diagram {
		for z, matrix := range smt {
			for y, line := range matrix {
				for x, c := range line {

					// count active neighbours
					activeNeighbours := 0
					neighbours := getNeighbours2(x, y, z, w)
					for _, n := range neighbours {
						found, ok := (*diagram)[n.w][n.z][n.y][n.x]
						if ok && found == '#' {
							activeNeighbours++
						}

						// check if neighbour is not on current diagram
						if c == '#' && !isInDiagram2(n.w, n.z, n.y, n.x, *diagram) {
							safeIncrement2(n.w, n.z, n.y, n.x, reverseNeighboursActiveCount)
						}
					}

					// register changes
					if c == '#' && !(activeNeighbours == 2 || activeNeighbours == 3) {
						changes = append(changes, change2{
							Coord: point2{x: x, y: y, z: z, w: w},
							val:   '.',
						})
					} else if c == '.' && activeNeighbours == 3 {
						changes = append(changes, change2{
							Coord: point2{x: x, y: y, z: z, w: w},
							val:   '#',
						})
					}

				}
			}
		}
	}
	for w, smt := range reverseNeighboursActiveCount {
		for z, matrix := range smt {
			for y, line := range matrix {
				for x, count := range line {
					if count == 3 {
						changes = append(changes, change2{
							Coord: point2{x: x, y: y, z: z, w: w},
							val:   '#',
						})
					}
				}
			}
		}
	}

	// apply changes
	for _, c := range changes {
		safeInsertRune2(c.val, c.Coord.w, c.Coord.z, c.Coord.y, c.Coord.x, *diagram)
	}
}

func countActive(diagram *map[int]map[int]map[int]rune) int {
	total := 0
	for _, matrix := range *diagram {
		for _, line := range matrix {
			for _, c := range line {
				if c == '#' {
					total++
				}
			}
		}
	}
	return total
}

func countActive2(diagram *map[int]map[int]map[int]map[int]rune) int {
	total := 0
	for _, smt := range *diagram {
		for _, matrix := range smt {
			for _, line := range matrix {
				for _, c := range line {
					if c == '#' {
						total++
					}
				}
			}
		}
	}
	return total
}

func part1(diagram map[int]map[int]map[int]rune) {
	for i := 0; i < 6; i++ {
		step(&diagram)
	}

	fmt.Printf("Part 1: %d\n", countActive(&diagram))
}

func part2(diagram map[int]map[int]map[int]map[int]rune) {
	for i := 0; i < 6; i++ {
		step2(&diagram)
	}

	fmt.Printf("Part 1: %d\n", countActive2(&diagram))
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	lines := strings.Split(content, "\n")

	diagram := make(map[int]map[int]map[int]rune) // z, y, x
	diagram[0] = make(map[int]map[int]rune)
	for y, line := range lines {
		diagram[0][y] = make(map[int]rune)
		for x, c := range line {
			diagram[0][y][x] = c
		}
	}

	diagram2 := make(map[int]map[int]map[int]map[int]rune) // w,z,y,x
	diagram2[0] = make(map[int]map[int]map[int]rune)
	diagram2[0][0] = make(map[int]map[int]rune)
	for y, line := range lines {
		diagram2[0][0][y] = make(map[int]rune)
		for x, c := range line {
			diagram2[0][0][y][x] = c
		}
	}

	part1(diagram)
	part2(diagram2)
}
