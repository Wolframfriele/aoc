package main

import (
	"errors"
	"fmt"
	"os"
)

type Coordinate struct {
	x, y int
}

func parseDirection(currentPos Coordinate, direction rune) (Coordinate, error) {
	if direction == '^' {
		return Coordinate{currentPos.x, currentPos.y + 1}, nil
	} else if direction == '>' {
		return Coordinate{currentPos.x + 1, currentPos.y}, nil
	} else if direction == 'v' {
		return Coordinate{currentPos.x, currentPos.y - 1}, nil
	} else if direction == '<' {
		return Coordinate{currentPos.x - 1, currentPos.y}, nil
	}
	return Coordinate{0, 0}, errors.New("Unknown direction input, expect one of: ^ > v <")
}

func solveA(input []byte) (visitedCount int) {
	visited := make(map[Coordinate]int)
	currentPos := Coordinate{0, 0}
	for _, char := range input {
		newPos, err := parseDirection(currentPos, rune(char))
		if err != nil {
			fmt.Printf("Value: %q led to error: %v \n", char, err)
		}
		visited[newPos] += 1
		currentPos = newPos
	}
	visitedCount = len(visited)
	return
}

func solveB(input []byte) (visitedCount int) {
	visited := make(map[Coordinate]int)
	santaPos := Coordinate{0, 0}
	roboPos := Coordinate{0, 0}
	for i, char := range input {
		if i%2 == 0 {
			newPos, err := parseDirection(santaPos, rune(char))
			if err != nil {
				fmt.Printf("Value: %q led to error: %v \n", char, err)
			}
			visited[newPos] += 1
			santaPos = newPos
		} else {
			newPos, err := parseDirection(roboPos, rune(char))
			if err != nil {
				fmt.Printf("Value: %q led to error: %v \n", char, err)
			}
			visited[newPos] += 1
			roboPos = newPos
		}
	}
	visitedCount = len(visited)
	return
}

func main() {
	input, err := os.ReadFile("2015/day03/input.txt")
	if err != nil {
		panic(err)
	}
	resultA := solveA(input)
	fmt.Printf("Part A: %v\n", resultA)

	resultB := solveB(input)
	fmt.Printf("Part B: %v\n", resultB)
}
