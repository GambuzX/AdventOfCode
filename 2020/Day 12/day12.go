package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type action struct {
	action byte
	amount int
}

type Ship struct {
	x, y       int
	xdir, ydir int
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func manhattanDistance(x1, y1, x2, y2 int) int {
	return Abs(x2-x1) + Abs(y2-y1)
}

func rotateLeft(x, y int) (int, int) {
	return -y, x
}

func rotateRight(x, y int) (int, int) {
	return y, -x
}

func move(ship *Ship, action *action) {
	switch action.action {
	case 'N':
		ship.y += action.amount
	case 'S':
		ship.y -= action.amount
	case 'E':
		ship.x += action.amount
	case 'W':
		ship.x -= action.amount
	case 'L':
		times := action.amount / 90
		for i := 0; i < times; i++ {
			ship.xdir, ship.ydir = rotateLeft(ship.xdir, ship.ydir)
		}
	case 'R':
		times := action.amount / 90
		for i := 0; i < times; i++ {
			ship.xdir, ship.ydir = rotateRight(ship.xdir, ship.ydir)
		}
	case 'F':
		left := ship.xdir == -1
		right := ship.xdir == 1
		top := ship.ydir == 1
		bot := ship.ydir == -1

		if left {
			ship.x -= action.amount
		}
		if right {
			ship.x += action.amount
		}
		if top {
			ship.y += action.amount
		}
		if bot {
			ship.y -= action.amount
		}
	}
}

func moveWithWaypoint(ship *Ship, waypoint *Ship, action *action) {
	switch action.action {
	case 'N':
		waypoint.y += action.amount
	case 'S':
		waypoint.y -= action.amount
	case 'E':
		waypoint.x += action.amount
	case 'W':
		waypoint.x -= action.amount
	case 'L':
		times := action.amount / 90
		for i := 0; i < times; i++ {
			waypoint.x, waypoint.y = rotateLeft(waypoint.x, waypoint.y)
		}
	case 'R':
		times := action.amount / 90
		for i := 0; i < times; i++ {
			waypoint.x, waypoint.y = rotateRight(waypoint.x, waypoint.y)
		}
	case 'F':
		xmove := waypoint.x * action.amount
		ymove := waypoint.y * action.amount
		ship.x += xmove
		ship.y += ymove
	}
}

func part1(actions []action) {
	ship := Ship{x: 0, y: 0, xdir: 1, ydir: 0}
	for _, action := range actions {
		move(&ship, &action)
	}
	dist := manhattanDistance(0, 0, ship.x, ship.y)
	fmt.Printf("Part 1: %d\n", dist)
}

func part2(actions []action) {
	ship := Ship{x: 0, y: 0, xdir: 1, ydir: 0}
	waypoint := Ship{x: 10, y: 1}
	for _, action := range actions {
		moveWithWaypoint(&ship, &waypoint, &action)
	}
	dist := manhattanDistance(0, 0, ship.x, ship.y)
	fmt.Printf("Part 2: %d\n", dist)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	actionsS := strings.Split(content, "\n")

	actions := make([]action, len(actionsS))
	for i, a := range actionsS {
		num, _ := strconv.Atoi(a[1:])
		actions[i] = action{
			action: a[0],
			amount: num,
		}
	}

	part1(actions)
	part2(actions)
}
