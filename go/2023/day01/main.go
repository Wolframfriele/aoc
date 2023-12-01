package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

// Find the calibration digit by combining the first and last digit in the string.
// Sum all calibration values

func findDigits(line string) int {
	// finds the first and last digit in a string
	// returns them as a number
	var digit1 rune
	var digit2 rune
	for _, char := range line {
		if unicode.IsDigit(char) {
			digit1 = char
			break
		}
	}
	for i := len(line) - 1; i >= 0; i-- {
		if unicode.IsDigit(rune(line[i])) {
			digit2 = rune(line[i])
			break
		}
	}
	result, err := strconv.Atoi(string(digit1) + string(digit2))
	if err != nil {
		panic(err)
	}
	return result
}

func solveA(input string) int {
	sum := 0
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		sum += findDigits(line)
	}
	return sum
}

func main() {
	input, err := os.ReadFile("2023/day01/input.txt")
	if err != nil {
		panic(err)
	}
	result := solveA(string(input))
	fmt.Println(result)
}
