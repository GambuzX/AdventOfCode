package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func part1(departTime int, buses []int) {

	var chosenBus int = 1
	minArrival := math.MaxInt64
	for _, bus := range buses {
		if bus == -1 {
			continue
		}
		arrivalTime := int(math.Ceil(float64(departTime)/float64(bus))) * bus
		if arrivalTime < minArrival {
			minArrival = arrivalTime
			chosenBus = bus
		}
	}
	fmt.Printf("Part 1: %d\n", chosenBus*(minArrival-departTime))
}

func part2(buses []int) {
	var res int64 = 0
	var inc int64 = int64(buses[0])
	for i, bus := range buses {
		if i == 0 || bus == -1 {
			continue
		}

		a, b := int64(i), int64(bus)
		for {
			res += inc
			if (res+a)%b == 0 {
				inc *= b
				break
			}
		}
	}
	fmt.Printf("Part 2: %d\n", res)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	lines := strings.Split(content, "\n")

	departTime, _ := strconv.Atoi(lines[0])
	busesS := strings.Split(lines[1], ",")

	buses := make([]int, 0)
	for _, bus := range busesS {
		num, err := strconv.Atoi(bus)
		if err == nil {
			buses = append(buses, num)
		} else {
			buses = append(buses, -1)
		}
	}
	part1(departTime, buses)
	part2(buses)
}
