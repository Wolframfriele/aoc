package main

import (
	"testing"
)

func TestParseInput(t *testing.T) {
	input := `467..11...
...*...#..
..35......`
	gotNumberStore, gotSymbolStore := parseInput(input)
	wantNumberStore := new(NumberStore)
	wantNumberStore.numbers = map[Coordinate]Number{
		{0, 0}: {value: 467, y: 0, start: 0},
		{0, 1}: {value: 467, y: 0, start: 0},
		{0, 2}: {value: 467, y: 0, start: 0},
		{0, 5}: {value: 11, y: 0, start: 5},
		{0, 6}: {value: 11, y: 0, start: 5},
		{2, 2}: {value: 35, y: 2, start: 2},
		{2, 3}: {value: 35, y: 2, start: 2},
	}
	wantNumberStore.adjacent = make(map[Number]int)
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
	wantSymbolStore.gears = map[Coordinate]map[int]bool{
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
	y    int
	x    int
	want Number
}

func TestParseNumber(t *testing.T) {
	inputs := []ParseNumberTest{
		{"..175..", 1, 2, Number{value: 175, y: 1, start: 2}},
		{"275..", 2, 1, Number{value: 275, y: 2, start: 0}},
		{"2.375..", 2, 2, Number{value: 375, y: 2, start: 2}},
		{".44..", 3, 2, Number{value: 44, y: 3, start: 1}},
		{".5..", 5, 1, Number{value: 5, y: 5, start: 1}},
		{"62.5", 6, 1, Number{value: 62, y: 6, start: 0}},
	}
	for _, input := range inputs {
		result := parseNumber(input.line, input.y, input.x)
		if result != input.want {
			t.Errorf("got %v, wanted %v from input %v", result, input.want, input.line)
		}
	}
}

type AddCoorTest struct {
	coorA    Coordinate
	CoorB    Coordinate
	expected Coordinate
}

func TestAddCoor(t *testing.T) {
	inputs := []AddCoorTest{
		{Coordinate{10, 10}, Coordinate{1, 1}, Coordinate{11, 11}},
		{Coordinate{10, 10}, Coordinate{-1, -1}, Coordinate{9, 9}},
	}
	for _, input := range inputs {
		got := input.coorA.addCoor(input.CoorB)
		if got != input.expected {
			t.Errorf("Got %v want %v", got, input.expected)
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

func TestSolveA(t *testing.T) {
	numbers, symbols := parseInput(example)
	got := solveA(numbers, symbols)
	want := 4361

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
