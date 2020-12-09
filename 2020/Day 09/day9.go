package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func validNum(num int, preamble map[int]bool) bool {
	for key := range preamble {
		missing := num - key
		if missing != key && preamble[missing] {
			return true
		}
	}
	return false
}

func part1(preamble map[int]bool, rest []int) int {
	for _, num := range rest {
		if !validNum(num, preamble) {
			fmt.Printf("Part 1: %d\n", num)
			return num
		}
		preamble[num] = true
	}
	return 0
}

func part2(target int, nums []int) {
	left, right := 0, 0
	currSum := 0

	for {
		for currSum < target { // expand right limit
			currSum += nums[right]
			right++
		}

		if currSum == target { // found solution
			min, max := nums[left], nums[left]
			for i := left + 1; i < right; i++ {
				if nums[i] < min {
					min = nums[i]
				}
				if nums[i] > max {
					max = nums[i]
				}
			}

			fmt.Printf("Part 2: %d\n", min+max)
			return
		}

		for currSum > target {
			currSum -= nums[left]
			left++
		}
	}
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)
	numsS := strings.Split(content, "\n")

	nums := make([]int, 0, 0)
	for _, s := range numsS {
		n, _ := strconv.Atoi(s)
		nums = append(nums, n)
	}

	preamble := make(map[int]bool)
	for i := 0; i < 25; i++ {
		preamble[nums[i]] = true
	}

	rest := nums[25:]
	target := part1(preamble, rest)
	part2(target, nums)
}
