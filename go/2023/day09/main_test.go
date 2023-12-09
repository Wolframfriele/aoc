package main

import (
	"testing"
)

const example = `0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
`

func TestSolveA(t *testing.T) {
	seq := parseInput(example)
	result := solveA(seq)
	want := 114
	if result != want {
		t.Errorf("Got %v, wanted %v", result, want)
	}
}

func TestSolveB(t *testing.T) {
	seq := parseInput(example)
	result := solveB(seq)
	want := 2
	if result != want {
		t.Errorf("Got %v, wanted %v", result, want)
	}
}
