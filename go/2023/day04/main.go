package main

import (
	"fmt"
	"os"
	"strings"
)

type Game struct {
	id      int
	winning []int
	have    []int
}

//
// func parseGame(line string) (game Game) {
// 	splitResult := strings.Split(line[5:], ": ")
// 	gameIndStr, allSelectionsStr := splitResult[0], splitResult[1]
// 	gameInd, err := strconv.Atoi(gameIndStr)
// 	if err != nil {
// 		fmt.Printf("Coult not convert %v to integer", gameIndStr)
// 	}
// 	allSelectionsSlice := strings.Split(allSelectionsStr, "; ")
// 	game.id = gameInd
// 	for _, selectionStr := range allSelectionsSlice {
//         if slices.Contains
// 		game.selections = append(game.selections, parseSelection(selectionStr))
// 	}
// 	return
// }

func Contains(checkIn []string, checkFor string) bool {
	for _, str := range checkIn {
		if str == checkFor {
			return true
		}
	}
	return false
}

func solveA(input string) (sum int) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if line == "" {
			break
		}
		split01 := strings.Split(line[8:], " | ")
		winning, have := split01[0], split01[1]
		winningSplit := strings.Fields(winning)
		haveSplit := strings.Fields(have)
		gamePoints := 0
		for _, code := range haveSplit {
			if Contains(winningSplit, code) {
				if gamePoints == 0 {
					gamePoints = 1
				} else {
					gamePoints *= 2
				}
			}
		}
		sum += gamePoints
	}
	return
}

//	func solveB(games []Game) (sum int) {
//		for _, game := range games {
//			maxSize := Selection{0, 0, 0}
//			for _, selection := range game.selections {
//				if selection.green > maxSize.green {
//					maxSize.green = selection.green
//				}
//				if selection.red > maxSize.red {
//					maxSize.red = selection.red
//				}
//				if selection.blue > maxSize.blue {
//					maxSize.blue = selection.blue
//				}
//			}
//			sum += maxSize.red * maxSize.blue * maxSize.green
//		}
//		return
//	}
func main() {
	input, err := os.ReadFile("2023/day04/input.txt")
	if err != nil {
		panic(err)
	}
	resultA := solveA(string(input))
	fmt.Printf("Result A: %v\n", resultA)

	// resultB := solveB(games)
	// fmt.Printf("Result B: %v\n", resultB)
}
