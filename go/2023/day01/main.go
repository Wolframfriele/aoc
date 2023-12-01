package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func getNumber(line string, i int, accept_word bool) rune {
	if unicode.IsDigit(rune(line[i])) {
		return rune(line[i])
	}
	if accept_word {
		validNumWords := [9]string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
		for numIndex, number := range validNumWords {
			if i+len(number) <= len(line) {
				if strings.Contains(line[i:i+len(number)], number) {
					// return the index + 1 to match position in string slice
					// Then add + '0' to match the string converted runes
					return rune(numIndex+1) + '0'
				}
			}
		}
	}
	return ' '
}

func findDigits(line string, accept_word bool) int {
	// finds the first and last digit in a string
	// returns them as a number
	var digit1 rune
	var digit2 rune
	for i := range line {
		digit := getNumber(line, i, accept_word)
		if digit != ' ' {
			digit1 = digit
			break
		}
	}
	for i := len(line) - 1; i >= 0; i-- {
		digit := getNumber(line, i, accept_word)
		if digit != ' ' {
			digit2 = digit
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
	// Find the calibration digit by combining the first and last digit in the string.
	// Sum all calibration values
	sum := 0
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		sum += findDigits(line, false)
	}
	return sum
}

func solveB(input string) int {
	// Find the calibratinon digits by combining the first and last digit in the string
	// words like one, two etc also represent digits
	// Sum the found calibration values
	sum := 0
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		sum += findDigits(line, true)
	}
	return sum
}

func main() {
	input, err := os.ReadFile("2023/day01/input.txt")
	if err != nil {
		panic(err)
	}
	resultA := solveA(string(input))
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(string(input))
	fmt.Printf("Result B: %v\n", resultB)
}
