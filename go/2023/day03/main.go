package main

import (
	"fmt"
	"os"
	"strconv"

	/* 	"strconv" */
	"strings"
	"unicode"
)

type NumberPos struct {
	line  int
	start int
	end   int
}

func findNumbers(lines []string) (numbers []NumberPos) {
	for y, line := range lines {
		inNum := false
		currentNum := NumberPos{}
		currentNum.line = y
		for i, char := range line {
			if inNum == false && unicode.IsDigit(char) {
				inNum = true
				currentNum.start = i
				// check around number
			} else if inNum && !unicode.IsDigit(char) {
				currentNum.end = i - 1
				numbers = append(numbers, currentNum)
				inNum = false
			}
		}
		if inNum {
			currentNum.end = len(line) - 1
			numbers = append(numbers, currentNum)
			inNum = false
		}
	}
	return
}

func isSymbol(char rune) bool {
	return !unicode.IsDigit(char) && char != '.'
}

func numberIsAdjecentToSymbol(num NumberPos, lines []string) bool {
	if num.line > 0 {
		y := num.line - 1
		if num.start > 0 && isSymbol(rune(lines[y][num.start-1])) {
			return true
		}
		for _, char := range lines[y][num.start : num.end+1] {
			if isSymbol(char) {
				return true
			}
		}
		if num.end+1 < len(lines[y]) && isSymbol(rune(lines[y][num.end+1])) {
			return true
		}
	}
	y := num.line
	if num.start > 0 && isSymbol(rune(lines[y][num.start-1])) {
		return true
	}
	if num.end+1 < len(lines[y]) && isSymbol(rune(lines[y][num.end+1])) {
		return true
	}
	if num.line+1 < len(lines) {
		y := num.line + 1
		if num.start > 0 && isSymbol(rune(lines[y][num.start-1])) {
			return true
		}
		for _, char := range lines[y][num.start : num.end+1] {
			if isSymbol(char) {
				return true
			}
		}
		if num.end+1 < len(lines[y]) && isSymbol(rune(lines[y][num.end+1])) {
			return true
		}
	}
	return false
}

func convertNumToInt(num NumberPos, lines []string) (number int) {
	number, err := strconv.Atoi(lines[num.line][num.start : num.end+1])
	if err != nil {
		panic(err)
	}
	return
}

func solveA(lines []string) (sum int) {
	numbers := findNumbers(lines)
	for _, num := range numbers {
		if numberIsAdjecentToSymbol(num, lines) {
			sum += convertNumToInt(num, lines)
		}
	}
	return
}

// func solveB(games []Game) (sum int) {
//
// 	return
// }

func main() {
	input, err := os.ReadFile("2023/day03/input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(input), "\n")
	resultA := solveA(lines)
	fmt.Printf("Result A: %v\n", resultA)

	// resultB := solveB(games)
	// fmt.Printf("Result B: %v\n", resultB)
}
