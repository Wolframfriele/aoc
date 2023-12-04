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
			fmt.Printf("Coult not convert (%v) to integer\n", numStr)
		}
		intSlice = append(intSlice, num)
	}
	return
}

func parseCard(line string) (card Card) {
	splitResult := strings.Split(line[5:], ": ")
	gameIndStr, cardNumbers := splitResult[0], splitResult[1]
	gameInd, err := strconv.Atoi(strings.TrimSpace(gameIndStr))
	if err != nil {
		fmt.Printf("Coult not convert (%v) to integer\n", gameIndStr)
	}
	card.id = gameInd
	splitNumbers := strings.Split(cardNumbers, " | ")
	first, second := splitNumbers[0], splitNumbers[1]

	card.first = convertToIntSlice(first)
	card.second = convertToIntSlice(second)

	return
}

func Contains(checkIn []int, checkFor int) bool {
	for _, num := range checkIn {
		if num == checkFor {
			return true
		}
	}
	return false
}

func solveA(cards map[int]Card) (sum int) {
	for _, card := range cards {
		cardPoints := 0
		for _, code := range card.second {
			if Contains(card.first, code) {
				if cardPoints == 0 {
					cardPoints = 1
				} else {
					cardPoints *= 2
				}
			}
		}
		sum += cardPoints
	}
	return
}

func solveB(cards map[int]Card) (amountOfCards int) {
	cardCopies := make(map[int]int)
	amountOfCards += len(cards)

	for i := 1; i <= len(cards); i++ {
		amountOfCards += cardCopies[i]
		matchCount := 0
		for _, code := range cards[i].second {
			if Contains(cards[i].first, code) {
				matchCount++
			}
		}
		for j := 1; j <= matchCount; j++ {
			cardCopies[cards[i].id+j] += 1 + 1*cardCopies[cards[i].id]
		}
	}
	return
}

func main() {
	input, err := os.ReadFile("2023/day04/input.txt")
	if err != nil {
		panic(err)
	}
	games := parseInput(string(input))
	resultA := solveA(games)
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(games)
	fmt.Printf("Result B: %v\n", resultB)
}
