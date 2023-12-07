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

func (c *Coordinate) addCoor(other Coordinate) Coordinate {
	newCoor := *c
	newCoor.Y += other.Y
	newCoor.X += other.X
	return newCoor
}

type Number struct {
	y     int
	start int
	value int
}

type NumberStore struct {
	numbers  map[Coordinate]Number
	adjacent map[Number]int
}

func (store *NumberStore) AddNumber(y, x int, n Number) {
	if store.numbers == nil {
		store.numbers = make(map[Coordinate]Number)
	}
	if store.adjacent == nil {
		store.adjacent = make(map[Number]int)
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

func parseNumber(line string, y, x int) (num Number) {
	temp := ".." + line + ".."
	start := x
	end := x + 5
	if !unicode.IsDigit(rune(temp[start+1])) {
		start = x + 2
	}
	if !unicode.IsDigit(rune(temp[start])) {
		start = x + 1
	}
	if !unicode.IsDigit(rune(temp[x+4])) {
		end = x + 4
	}
	if !unicode.IsDigit(rune(temp[x+3])) {
		end = x + 3
	}

	value, err := strconv.Atoi(temp[start:end])
	if err != nil {
		panic(err)
	}
	num.value = value
	num.start = start - 2
	num.y = y
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
				numbersStore.AddNumber(y, x, parseNumber(line, y, x))
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
		_, ok := store.all[coor.addCoor(neighbor)]
		if ok {
			return true
		}
	}
	return false
}

func findAdjacentNumber(coor Coordinate, store *NumberStore) (numbers []int) {
	for _, neighbor := range check {
		num, ok := store.numbers[coor.addCoor(neighbor)]
		if ok {
			numbers = append(numbers, num.value)
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
	for num := range numStore.adjacent {
		sum += num.value
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
