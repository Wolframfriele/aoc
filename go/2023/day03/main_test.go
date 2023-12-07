package main

import (
	"testing"
)

const example = `467..114..
..*.......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

func TestParseInput(t *testing.T) {
	input := `467..11...
...*...#..
..35......`
	gotNumberStore, gotSymbolStore := parseInput(input)
	wantNumberStore := new(NumberStore)
	wantNumberStore.numbers = map[Coordinate]int{
		{0, 0}: 467,
		{0, 1}: 467,
		{0, 2}: 467,
		{0, 5}: 11,
		{0, 6}: 11,
		{2, 2}: 35,
		{2, 3}: 35,
	}
	wantNumberStore.adjacent = make(map[int]int)
	for i := range gotNumberStore.numbers {
		if gotNumberStore.numbers[i] != wantNumberStore.numbers[i] {
			t.Errorf("got %v, wanted %v", gotNumberStore.numbers[i], wantNumberStore.numbers[i])
		}
	}
	wantSymbolStore := new(SymbolStore)
	wantSymbolStore.all = map[Coordinate]bool{
		{1, 3}: true,
		{1, 7}: true,
	}
	wantSymbolStore.gears = map[Coordinate][]int{
		{1, 3}: {},
	}
	for i := range gotSymbolStore.all {
		if gotSymbolStore.all[i] != wantSymbolStore.all[i] {
			t.Errorf("got %v, wanted %v", gotSymbolStore.all[i], wantSymbolStore.all[i])
		}
	}
	for i := range gotSymbolStore.gears {
		_, ok := wantSymbolStore.gears[i]
		if !ok {
			t.Errorf("got %v, wanted %v", gotSymbolStore.gears[i], wantSymbolStore.gears[i])
		}
	}
}

type ParseNumberTest struct {
	line string
	x    int
	want int
}

func TestParseNumber(t *testing.T) {
	inputs := []ParseNumberTest{
		{"..175..", 2, 175},
		{"275..", 1, 275},
		{"2.375..", 2, 375},
		{".44..", 2, 44},
		{".5..", 1, 5},
		{"62.5", 1, 62},
	}
	for _, input := range inputs {
		result := parseNumber(input.line, input.x)
		if result != input.want {
			t.Errorf("got %v, wanted %v from input %v", result, input.want, input.line)
		}
	}
}

type FindAdacentTest struct {
	coor Coordinate
	want bool
}

func TestFindAdjecent(t *testing.T) {
	inputStore := new(SymbolStore)
	inputStore.all = map[Coordinate]bool{
		{1, 3}: true,
		{1, 7}: true,
	}
	inputs := []FindAdacentTest{
		{Coordinate{1, 4}, true},
		{Coordinate{2, 6}, true},
		{Coordinate{10, 10}, false},
	}
	for _, input := range inputs {
		result := findAdjacentSymbols(input.coor, inputStore)
		if result != input.want {
			t.Errorf("got %v, wanted %v", result, input.want)
		}
	}
}

func TestSolveA(t *testing.T) {
	numbers, symbols := parseInput(example)
	got := solveA(numbers, symbols)
	want := 4361

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
	input := `467....412
..*.......
1.35..633.
......#.22
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`
	numbers, symbols = parseInput(input)
	got = solveA(numbers, symbols)
	want = 4361

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

func TestSolveB(t *testing.T) {
	numbers, symbols := parseInput(example)
	got := solveB(numbers, symbols)
	want := 467835

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}
