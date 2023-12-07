package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type Coordinate struct {
	Y int
	X int
}

type NumberStore struct {
	numbers  map[Coordinate]int
	adjacent map[int]int
}

func (store *NumberStore) AddNumber(y, x, n int) {
	if store.numbers == nil {
		store.numbers = make(map[Coordinate]int)
	}
	if store.adjacent == nil {
		store.adjacent = make(map[int]int)
	}
	store.numbers[Coordinate{y, x}] = n
}

type SymbolStore struct {
	gears map[Coordinate]map[int]bool
	all   map[Coordinate]bool
}

func (store *SymbolStore) AddSymbol(y, x int, s rune) {
	if store.all == nil {
		store.all = map[Coordinate]bool{}
	}
	if store.gears == nil {
		store.gears = map[Coordinate]map[int]bool{}
	}
	if s == '*' {
		store.all[Coordinate{y, x}] = true
		store.gears[Coordinate{y, x}] = map[int]bool{}
	} else {
		store.all[Coordinate{y, x}] = true
	}
}

func parseNumber(line string, x int) (num int) {
	temp := ".." + line + ".."
	start := x
	end := x + 5
	if !unicode.IsDigit(rune(temp[start+1])) {
		start = x + 2
	}
	if !unicode.IsDigit(rune(temp[x+3])) {
		end = x + 3
	}
	trimmed := strings.Trim(temp[start:end], ".-+=#&/%$@*<>!+_")
	num, err := strconv.Atoi(trimmed)
	if err != nil {
		panic(err)
	}
	return
}

func parseInput(input string) (numbersStore NumberStore, symbolStore SymbolStore) {
	lines := strings.Split(string(input), "\n")
	for y, line := range lines {
		if len(line) == 0 {
			continue
		}
		for x, char := range line {
			if char == '.' {
				continue
			} else if unicode.IsDigit(char) {
				numbersStore.AddNumber(y, x, parseNumber(line, x))
			} else {
				symbolStore.AddSymbol(y, x, char)
			}
		}
	}
	return
}

var check = []Coordinate{
	{-1, 0},
	{-1, 1},
	{0, 1},
	{1, 1},
	{1, 0},
	{1, -1},
	{0, -1},
	{-1, -1},
}

func findAdjacentSymbols(coor Coordinate, store *SymbolStore) bool {
	for _, neighbor := range check {
		neigborCoor := coor
		neigborCoor.Y += neighbor.Y
		neigborCoor.X += neighbor.X
		_, ok := store.all[neigborCoor]
		if ok {
			return true
		}
	}
	return false
}

func findAdjacentNumber(coor Coordinate, store *NumberStore) (numbers []int) {
	for _, neighbor := range check {
		neigborCoor := coor
		neigborCoor.Y += neighbor.Y
		neigborCoor.X += neighbor.X
		num, ok := store.numbers[neigborCoor]
		if ok {
			numbers = append(numbers, num)
		}
	}
	return
}

func solveA(numStore NumberStore, symStore SymbolStore) (sum int) {
	for coor, num := range numStore.numbers {
		if findAdjacentSymbols(coor, &symStore) {
			numStore.adjacent[num] += 1
		}
	}
	for num, count := range numStore.adjacent {
		if count > 0 {
			sum += count * num
		}
	}
	return
}

func solveB(numStore NumberStore, symStore SymbolStore) (sum int) {
	for coor := range symStore.gears {
		neighbors := findAdjacentNumber(coor, &numStore)
		if len(neighbors) > 0 {
			for _, neighbor := range neighbors {
				symStore.gears[coor][neighbor] = true
			}
		}
	}
	for _, neighbors := range symStore.gears {
		if len(neighbors) == 2 {
			mul := 1
			for key := range neighbors {
				mul *= key
			}
			sum += mul
		}
	}

	return
}

func main() {
	input, err := os.ReadFile("2023/day03/input.txt")
	if err != nil {
		panic(err)
	}
	numbers, symbols := parseInput(string(input))
	resultA := solveA(numbers, symbols)
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(numbers, symbols)
	fmt.Printf("Result B: %v\n", resultB)
}
