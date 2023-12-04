package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Card struct {
	id     int
	first  []int
	second []int
}

func parseInput(input string) map[int]Card {
	cards := make(map[int]Card)
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if len(line) > 0 {
			card := parseCard(line)
			cards[card.id] = card
		}
	}
	return cards
}

func convertToIntSlice(stringSlice string) (intSlice []int) {
	split := strings.Fields(stringSlice)
	for _, numStr := range split {
		num, err := strconv.Atoi(numStr)
		if err != nil {
			fmt.Printf("Coult not convert %v to integer", numStr)
		}
		intSlice = append(intSlice, num)
	}
	return
}

func parseCard(line string) (card Card) {
	splitResult := strings.Split(line[5:], ": ")
	gameIndStr, cardNumbers := splitResult[0], splitResult[1]
	gameInd, err := strconv.Atoi(gameIndStr)
	if err != nil {
		fmt.Printf("Coult not convert %v to integer", gameIndStr)
	}
	card.id = gameInd
	splitNumbers := strings.Split(cardNumbers, " | ")
	first, second := splitNumbers[0], splitNumbers[1]

	card.first = convertToIntSlice(first)
	card.second = convertToIntSlice(second)

	return
}

func Contains(checkIn []int, checkFor int) bool {
	for _, str := range checkIn {
		if str == checkFor {
			return true
		}
	}
	return false
}

func solveA(cards map[int]Card) (sum int) {
	for _, card := range cards {
		gamePoints := 0
		for _, code := range card.second {
			if Contains(card.first, code) {
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
//		//		return
//	}
func main() {
	input, err := os.ReadFile("2023/day04/input.txt")
	if err != nil {
		panic(err)
	}
	games := parseInput(string(input))
	resultA := solveA(games)
	fmt.Printf("Result A: %v\n", resultA)

	// resultB := solveB(games)
	// fmt.Printf("Result B: %v\n", resultB)
}
