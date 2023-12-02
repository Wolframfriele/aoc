package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Selection struct {
	red   int
	green int
	blue  int
}

type Game struct {
	id         int
	selections []Selection
}

func parseInput(input string) (games []Game) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if line == "" {
			break
		}
		splitResult := strings.Split(line[5:], ": ")
		gameIndStr, allSelectionsStr := splitResult[0], splitResult[1]
		gameInd, err := strconv.Atoi(gameIndStr)
		if err != nil {
			fmt.Printf("Coult not convert %v to integer", gameIndStr)
		}
		allSelectionsSlice := strings.Split(allSelectionsStr, "; ")
		var selections []Selection
		game := Game{gameInd, selections}
		for _, selectionStr := range allSelectionsSlice {
			kubes := strings.Split(selectionStr, ", ")
			selection := Selection{}
			for _, kube := range kubes {
				valueKeyStr := strings.Split(kube, " ")
				switch valueKeyStr[1] {
				case "green":
					amount, err := strconv.Atoi(valueKeyStr[0])
					if err != nil {
						fmt.Printf("Could not convert %v to interger in game %v.\n", valueKeyStr, gameIndStr)
						break
					}
					selection.green = amount
				case "blue":
					amount, err := strconv.Atoi(valueKeyStr[0])
					if err != nil {
						fmt.Printf("Could not convert to number for %v in game %v", valueKeyStr, gameIndStr)
						break
					}
					selection.blue = amount
				case "red":
					amount, err := strconv.Atoi(valueKeyStr[0])
					if err != nil {
						fmt.Printf("Could not convert to number for %v in game %v", valueKeyStr, gameIndStr)
						break
					}
					selection.red = amount
				}
			}
			game.selections = append(game.selections, selection)
		}
		games = append(games, game)
	}
	return
}

func solveA(games []Game, bagContains Selection) (sum int) {
	// sum the id's for possible games
	// given an amount of colored cubes
	for _, game := range games {
		posible := true
		for _, selection := range game.selections {
			if selection.green > bagContains.green || selection.blue > bagContains.blue || selection.red > bagContains.red {
				posible = false
				break
			}
		}
		if posible {
			sum += game.id
		}
	}
	return
}

func solveB(games []Game) (sum int) {
	for _, game := range games {
		maxSize := Selection{0, 0, 0}
		for _, selection := range game.selections {
			if selection.green > maxSize.green {
				maxSize.green = selection.green
			}
			if selection.red > maxSize.red {
				maxSize.red = selection.red
			}
			if selection.blue > maxSize.blue {
				maxSize.blue = selection.blue
			}
		}
		sum += maxSize.red * maxSize.blue * maxSize.green
	}
	return
}

func main() {
	input, err := os.ReadFile("2023/day02/input.txt")
	if err != nil {
		panic(err)
	}
	games := parseInput(string(input))
	resultA := solveA(games, Selection{12, 13, 14})
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(games)
	fmt.Printf("Result B: %v\n", resultB)
}
