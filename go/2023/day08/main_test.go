package main

import (
	"testing"
)

const example = `RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
`

const example2 = `LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
`

const example3 = `LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
`

func TestSolveA(t *testing.T) {
	route, graph := parseInput(example)
	result := solveA(route, graph)
	want := 2
	if result != want {
		t.Errorf("Got %v, wanted %v", result, want)
	}
	route2, graph2 := parseInput(example2)
	result2 := solveA(route2, graph2)
	want2 := 6
	if result2 != want2 {
		t.Errorf("Got %v, wanted %v", result2, want2)
	}
}

func TestSolveB(t *testing.T) {
	route, graph := parseInput(example3)
	result := solveB(route, graph)
	want := 6
	if result != want {
		t.Errorf("Got %v, wanted %v", result, want)
	}
}

type PrimeFactorTests struct {
	num     int
	factors map[int]int
}

func TestPrimeFactors(t *testing.T) {
	tests := []PrimeFactorTests{
		{6, map[int]int{2: 1, 3: 1}},
		{12, map[int]int{2: 2, 3: 1}},
		{7, map[int]int{7: 1}},
		{58742, map[int]int{2: 1, 23: 1, 1277: 1}},
		{587427364, map[int]int{2: 2, 29: 1, 59: 1, 85831: 1}},
	}
	for _, test := range tests {
		got := primeFactors(test.num)
		if len(got) != len(test.factors) {
			t.Errorf("Got %v, wanted %v", got, test.factors)
		}
		for i := range got {
			if got[i] != test.factors[i] {
				t.Errorf("Got %v, wanted %v", got[i], test.factors[i])
			}
		}
	}
}
