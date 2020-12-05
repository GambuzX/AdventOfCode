package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func seatToRow(seat string) int {
	low, high := 0, 127
	for i := 0; i < 7; i++ {
		diff := int(math.Ceil(float64(high-low) / 2))
		if seat[i] == 'F' {
			high -= diff
		} else if seat[i] == 'B' {
			low += diff
		}
	}
	return low
}

func seatToCol(seat string) int {
	low, high := 0, 7
	for i := 0; i < 3; i++ {
		diff := int(math.Ceil(float64(high-low) / 2))
		if seat[i+7] == 'L' {
			high -= diff
		} else if seat[i+7] == 'R' {
			low += diff
		}
	}
	return low
}

func seatID(row, col int) int {
	return row*8 + col
}

func part1(seats []string) {
	highestSeatID := 0
	for _, seat := range seats {
		row := seatToRow(seat)
		col := seatToCol(seat)
		seatID := seatID(row, col)
		if seatID > highestSeatID {
			highestSeatID = seatID
		}
	}

	fmt.Printf("Part 1: %d\n", highestSeatID)
}

func part2(seats []string) {
	minSeat := 127 * 7
	validSeats := make(map[int]bool)
	for _, seat := range seats {
		row := seatToRow(seat)
		col := seatToCol(seat)

		currID := seatID(row, col)
		validSeats[currID] = true
		if currID < minSeat {
			minSeat = currID
		}
	}

	for i := minSeat + 1; i < 127*7; i++ {

		if _, currOk := validSeats[i]; currOk {
			continue
		}
		if _, beforeOk := validSeats[i-1]; !beforeOk {
			continue
		}
		if _, afterOk := validSeats[i+1]; !afterOk {
			continue
		}
		fmt.Printf("Part 2: %d\n", i)
		return
	}

}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	seats := strings.Split(content, "\n")

	part1(seats)
	part2(seats)

}
