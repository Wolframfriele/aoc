package main

import (
	"fmt"
	"os"
	"strconv"

	/* 	"strconv" */
	"strings"
	"unicode"
)

func parseInput(input string) (numbers map[Coordinate]Number, symbols map[Coordinate]bool) {
	lines := strings.Split(string(input), "\n")
	for y, line := range lines {
		if len(line) == 0 {
			continue
		}
		inNum := false
		for x, char := range line {
			if char == '.' {
				continue
			} else if unicode.IsDigit(char) {
				inNum := true
			}
		}
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
