package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"regexp"
	"strconv"
	"strings"
)

type rule struct {
	name                   string
	min1, max1, min2, max2 int
}

type ticket struct {
	nums []int
}

func invalidTicket(t *ticket, rules []rule) (bool, int) {
	total := 0
	valid := true
	for _, num := range t.nums {
		found := false
		for _, rule := range rules {
			if inRange(num, rule) {
				found = true
				break
			}
		}
		if !found {
			total += num
			valid = false
		}
	}
	return valid, total
}

func inRange(num int, r rule) bool {
	return (num >= r.min1 && num <= r.max1) || (num >= r.min2 && num <= r.max2)
}

func part1(rules []rule, tickets []ticket) {
	total := 0
	for i := 1; i < len(tickets); i++ {
		ticket := &tickets[i]
		_, t := invalidTicket(ticket, rules)
		total += t
	}

	fmt.Printf("Part 1: %d\n", total)
}

func determineRules(possibilities [20]map[string]bool) [20]string {
	var res [20]string
	for i := 0; i < 20; i++ {
		for j, p := range possibilities {
			if len(p) == 1 {
				name := reflect.ValueOf(p).MapKeys()[0].String()
				res[j] = name
				for k, other := range possibilities {
					if k != j {
						delete(other, name)
					}
				}
			}
		}
	}
	return res
}

func part2(rules []rule, tickets []ticket) {
	var possibilities [20]map[string]bool
	for i := range possibilities {
		possibilities[i] = make(map[string]bool)
	}

	// get possibilities for each field
	filledPossibilities := false
	for i := 1; i < len(tickets); i++ {
		t := &tickets[i]
		valid, _ := invalidTicket(t, rules)
		if !valid {
			continue
		}

		if !filledPossibilities {
			for j, num := range t.nums {
				for _, rule := range rules {
					if inRange(num, rule) {
						possibilities[j][rule.name] = true
					}
				}
			}
			filledPossibilities = true
			continue
		}

		for j, num := range t.nums {
			deleted := 0
			for _, rule := range rules {
				if _, ok := possibilities[j][rule.name]; !ok { // skip if not a possibility
					continue
				}

				// decide whether to keep the rule or not
				if !inRange(num, rule) {
					delete(possibilities[j], rule.name)
					deleted++
				}
			}
		}
	}

	// determine only solution
	res := determineRules(possibilities)
	for _, r := range res {
		fmt.Println(r)
	}

	total := 1
	for i, name := range res {
		if strings.Contains(name, "departure") {
			total *= tickets[0].nums[i]
		}
	}
	fmt.Printf("Part 2: %d\n", total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)

	rules := make([]rule, 0)
	re := regexp.MustCompile(`(?m)(.*):\s(\d*)-(\d*)\sor\s(\d*)-(\d*)`)
	for _, match := range re.FindAllStringSubmatch(content, -1) {
		min1, _ := strconv.Atoi(match[2])
		max1, _ := strconv.Atoi(match[3])
		min2, _ := strconv.Atoi(match[4])
		max2, _ := strconv.Atoi(match[5])
		rules = append(rules, rule{
			name: match[1],
			min1: min1,
			min2: min2,
			max1: max1,
			max2: max2,
		})
	}

	tickets := make([]ticket, 0)
	re = regexp.MustCompile(`(?m)^([\d,]+)$`)
	for _, match := range re.FindAllStringSubmatch(content, -1) {
		numsS := strings.Split(match[0], ",")
		nums := make([]int, len(numsS))
		for i, s := range numsS {
			num, _ := strconv.Atoi(s)
			nums[i] = num
		}
		tickets = append(tickets, ticket{nums: nums})
	}

	part1(rules, tickets)
	part2(rules, tickets)
}
