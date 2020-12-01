package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func ex1(nums []int, m map[int]bool, target int) {
	for _, num := range nums {
		missing := target - num
		if m[missing] {
			fmt.Println(num * missing)
			break
		}
	}
}

// good thing it does not have to be efficient :)
func ex2(nums []int, m map[int]bool, target int) {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			missing := target - nums[i] - nums[j]
			if m[missing] {
				fmt.Println(missing * nums[i] * nums[j])
				return
			}
		}
	}
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)

	lines := strings.Split(content, "\n")
	var nums []int = make([]int, len(lines), len(lines))
	for i, line := range lines {
		nums[i], _ = strconv.Atoi(line)
	}

	var m map[int]bool = make(map[int]bool)
	for _, num := range nums {
		m[num] = true
	}

	target := 2020
	ex1(nums, m, target)
	ex2(nums, m, target)
}
