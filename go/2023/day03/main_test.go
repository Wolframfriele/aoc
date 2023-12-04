package main

import (
	"strings"
	"testing"
)

func TestFindNumbers(t *testing.T) {
	input := `467..114..
...*......
..35..633.`
	lines := strings.Split(input, "\n")
	result := findNumbers(lines)
	want := []NumberPos{
		{line: 0, start: 0, end: 2},
		{line: 0, start: 5, end: 7},
		{line: 2, start: 2, end: 3},
		{line: 2, start: 6, end: 8},
	}
	for i, got := range result {
		if got != want[i] {
			t.Errorf("got %v, wanted %v", got, want[i])
		}
	}
}

func TestNumberAdjecent(t *testing.T) {
	input := `467..114..
...*......
..35..633.`
	lines := strings.Split(input, "\n")
	want := true
	got := numberIsAdjecentToSymbol(NumberPos{line: 0, start: 0, end: 2}, lines)
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
	want = false
	got = numberIsAdjecentToSymbol(NumberPos{line: 0, start: 5, end: 7}, lines)
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

func TestSolveA(t *testing.T) {
	input := `467..114..
..*.......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`
	lines := strings.Split(input, "\n")
	got := solveA(lines)
	want := 4361

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}
