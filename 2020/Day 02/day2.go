package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
)

type pwdPolicy struct {
	min int
	max int
	c   byte
	s   string
}

func validPwd(pwd pwdPolicy) bool {
	count := 0
	for i := range pwd.s {
		if pwd.s[i] == pwd.c {
			count++
		}
	}

	return count >= pwd.min && count <= pwd.max
}

func validPwd2(pwd pwdPolicy) bool {
	var pos1, pos2 bool

	if pwd.min-1 < len(pwd.s) {
		pos1 = pwd.s[pwd.min-1] == pwd.c
	}

	if pwd.max-1 < len(pwd.s) {
		pos2 = pwd.s[pwd.max-1] == pwd.c
	}

	return (pos1 && !pos2) || (!pos1 && pos2)
}

func ex1(passwords []pwdPolicy) {
	total := 0
	for _, pwd := range passwords {
		if validPwd(pwd) {
			total++
		}
	}
	fmt.Println(total)
}

func ex2(passwords []pwdPolicy) {
	total := 0
	for _, pwd := range passwords {
		if validPwd2(pwd) {
			total++
		}
	}
	fmt.Println(total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)

	var passwords []pwdPolicy
	var re = regexp.MustCompile(`(?m)(\d+)-(\d+)\s([a-z]):\s([a-z]+)`)
	for _, match := range re.FindAllStringSubmatch(content, -1) {
		min, _ := strconv.Atoi(match[1])
		max, _ := strconv.Atoi(match[2])
		passwords = append(passwords, pwdPolicy{
			min: min,
			max: max,
			c:   match[3][0],
			s:   match[4],
		})
	}

	ex1(passwords)
	ex2(passwords)
}
