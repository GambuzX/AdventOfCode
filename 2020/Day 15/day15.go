package main

import "fmt"

type numinfo struct {
	firstTime            bool
	index, previousIndex int
}

func getNthNumberSpoken(n int, nums []int) int {
	spoken := make(map[int]numinfo)
	last := -1
	for i := 0; i < n; i++ {
		if i < len(nums) {
			entry, seen := spoken[nums[i]]
			if seen {
				spoken[nums[i]] = numinfo{
					firstTime:     false,
					index:         i,
					previousIndex: entry.index,
				}
			} else {
				spoken[nums[i]] = numinfo{
					firstTime: true,
					index:     i,
				}
			}
			last = nums[i]
			continue
		}

		// choose next number
		entry := spoken[last]
		var num int
		if entry.firstTime {
			num = 0
		} else {
			num = entry.index - entry.previousIndex
		}

		// update state
		numEntry, seen := spoken[num]
		if seen {
			spoken[num] = numinfo{
				firstTime:     false,
				index:         i,
				previousIndex: numEntry.index,
			}
		} else {
			spoken[num] = numinfo{
				firstTime: true,
				index:     i,
			}
		}
		last = num
	}
	return last
}

func main() {
	input := []int{5, 2, 8, 16, 18, 0, 1}
	fmt.Printf("Part 1: %d\n", getNthNumberSpoken(2020, input))
	fmt.Printf("Part 2: %d\n", getNthNumberSpoken(30000000, input))
}
