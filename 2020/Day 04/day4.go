package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func getRequiredFields() map[string]func(string) bool {
	return map[string]func(string) bool{
		"byr": validByr,
		"iyr": validIyr,
		"eyr": validEyr,
		"hgt": validHgt,
		"hcl": validHcl,
		"ecl": validEcl,
		"pid": validPid,
	}
}

func validByr(inp string) bool {
	if len(inp) != 4 {
		return false
	}
	num, err := strconv.Atoi(inp)
	if err != nil {
		return false
	}
	return num >= 1920 && num <= 2002
}

func validIyr(inp string) bool {
	if len(inp) != 4 {
		return false
	}
	num, err := strconv.Atoi(inp)
	if err != nil {
		return false
	}
	return num >= 2010 && num <= 2020
}

func validEyr(inp string) bool {
	if len(inp) != 4 {
		return false
	}
	num, err := strconv.Atoi(inp)
	if err != nil {
		return false
	}
	return num >= 2020 && num <= 2030
}

func validHgt(inp string) bool {
	if len(inp) < 3 {
		return false
	}

	numS := inp[:len(inp)-2]
	prefix := inp[len(inp)-2:]
	if prefix == "cm" {
		num, err := strconv.Atoi(numS)
		if err != nil {
			return false
		}
		return num >= 150 && num <= 193
	} else if prefix == "in" {
		num, err := strconv.Atoi(numS)
		if err != nil {
			return false
		}
		return num >= 59 && num <= 76
	}
	return false
}

func validHcl(inp string) bool {
	if len(inp) != 7 {
		return false
	}

	if inp[0] != '#' {
		return false
	}

	for i := 1; i < len(inp); i++ {
		if !((inp[i] >= 'a' && inp[i] <= 'f') || (inp[i] >= '0' && inp[i] <= '9')) {
			return false
		}
	}
	return true
}

func validEcl(inp string) bool {
	valid := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	for _, v := range valid {
		if inp == v {
			return true
		}
	}
	return false
}

func validPid(inp string) bool {
	if len(inp) != 9 {
		return false
	}

	_, err := strconv.Atoi(inp)
	return err == nil
}

func ex1(passports []map[string]string) {
	total := 0
	required := getRequiredFields()

	for _, p := range passports {
		valid := true
		for field := range required {
			if _, ok := p[field]; !ok {
				valid = false
				break
			}
		}

		if valid {
			total++
		}
	}

	fmt.Printf("Part 1: %d\n", total)
}

func ex2(passports []map[string]string) {
	total := 0
	required := getRequiredFields()

	for _, p := range passports {
		valid := true
		for field, f := range required {
			val, fieldExists := p[field]
			if !fieldExists {
				valid = false
				break
			}

			if !f(val) {
				valid = false
				break
			}
		}

		if valid {
			total++
		}
	}

	fmt.Printf("Part 2: %d\n", total)
}

func main() {
	dat, _ := ioutil.ReadFile("./input.txt")
	content := string(dat)

	passports := make([]map[string]string, 1, 1)
	passportsLines := strings.Split(content, "\n\n")
	for _, passp := range passportsLines {

		fields := make(map[string]string)

		var re = regexp.MustCompile(`(?m)([a-z]*):([^\s]*)`)
		for _, match := range re.FindAllStringSubmatch(passp, -1) {
			fields[match[1]] = match[2]
		}

		passports = append(passports, fields)
	}

	ex1(passports)
	ex2(passports)
}
