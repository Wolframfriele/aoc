package main

import (
	"fmt"
	"os"
)

func countFloor(input string, find_first_floor bool, floor_to_find int) int {
	var floor int
	for pos, char := range input {
		if char == '(' {
			floor++
		} else if char == ')' {
			floor--
		}
		if find_first_floor == true && floor == floor_to_find {
			return int(pos) + 1
		}
	}
	return floor
}

func solveA(input string) int {
	return countFloor(input, false, 0)
}

func solveB(input string) int {
	return countFloor(input, true, -1)
}

func main() {
	input, err := os.ReadFile("2015/day01/input.txt")
	if err != nil {
		panic(err)
	}
	resultA := solveA(string(input))
	fmt.Println(resultA)

	resultB := solveB(string(input))
	fmt.Println(resultB)
}
