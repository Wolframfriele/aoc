package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var cardValueA = map[rune]int{
	'A': 14, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1,
}

var cardValueB = map[rune]int{
	'A': 14, 'K': 12, 'Q': 11, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2,
}

type Hand struct {
	order     string
	cardCount map[rune]int
	rank      int
	bid       int
}

func (h *Hand) handFromString(str string, partB bool) {
	if h.cardCount == nil {
		h.cardCount = make(map[rune]int)
	}
	inputs := strings.Fields(str)
	h.order = inputs[0]
	for _, char := range inputs[0] {
		h.cardCount[char]++
	}
	bid, err := strconv.Atoi(inputs[1])
	if err != nil {
		panic(err)
	}
	h.bid = bid
	if partB {
		h.rankHandB()
	} else {
		h.rankHandA()
	}
}

func (h *Hand) rankHandA() {
	switch len(h.cardCount) {
	case 1:
		h.rank = 7
	case 2:
		// options: fourOfKind, fullHouse
		for _, count := range h.cardCount {
			if count == 4 || count == 1 {
				h.rank = 6
			} else {
				h.rank = 5
			}
		}
	case 3:
		// options: threeOfKind, 2 pair
		isThree := false
		for _, count := range h.cardCount {
			if count == 3 {
				isThree = true
			}
		}
		if isThree {
			// Three of a kind
			h.rank = 4
		} else {
			// 2 pair
			h.rank = 3
		}
	case 4:
		// options: pair
		h.rank = 2
	case 5:
		// high card:
		h.rank = 1
	}
}

func (h *Hand) rankHandB() {
	jokerCount := h.cardCount['J']
	if jokerCount > 0 {
		highestCount := 0
		highestType := ' '
		for card, count := range h.cardCount {
			if card != 'J' && count > highestCount {
				highestCount = count
				highestType = card
			}
		}
		h.cardCount[highestType] += jokerCount
		delete(h.cardCount, 'J')
		h.rankHandA()
	} else {
		h.rankHandA()
	}
}

func parseInputA(input string) (hands []Hand) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if len(line) > 0 {
			h := new(Hand)
			h.handFromString(line, false)
			hands = append(hands, *h)
		}
	}
	return
}

func solveA(hands []Hand) (totalWin int) {
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].rank != hands[j].rank {
			return hands[i].rank < hands[j].rank
		} else {
			for x := range hands[i].order {
				if hands[i].order[x] != hands[j].order[x] {
					return cardValueA[rune(hands[i].order[x])] < cardValueA[rune(hands[j].order[x])]
				}
			}
			panic("Cards have the same rank")
		}
	})
	for i, hand := range hands {
		totalWin += (i + 1) * hand.bid
	}
	return
}

func parseInputB(input string) (hands []Hand) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		h := new(Hand)
		h.handFromString(line, true)
		hands = append(hands, *h)
	}
	return
}

func solveB(hands []Hand) (totalWin int) {
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].rank != hands[j].rank {
			return hands[i].rank < hands[j].rank
		} else {
			for x := range hands[i].order {
				if hands[i].order[x] != hands[j].order[x] {
					return cardValueB[rune(hands[i].order[x])] < cardValueB[rune(hands[j].order[x])]
				}
			}
			panic("Cards have the same rank")
		}
	})
	for i, hand := range hands {
		totalWin += (i + 1) * hand.bid
	}
	return
}

const example = `JAJ43 10
JA6J4 10`

func main() {
	input, err := os.ReadFile("2023/day07/input.txt")
	if err != nil {
		panic(err)
	}
	handsA := parseInputA(string(input))
	resultA := solveA(handsA)
	fmt.Println("Solution to part A: ", resultA)

	handsB := parseInputB(string(input))
	resultB := solveB(handsB)
	fmt.Println("Solution to part B: ", resultB)
}
