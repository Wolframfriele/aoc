package main

import (
	"testing"
)

const example = `Time:      7  15   30
Distance:  9  40  200`

func TestParseInput(t *testing.T) {
	got := parseInput(string(example))
	want := []Race{
		{7, 9},
		{15, 40},
		{30, 200},
	}
	for i := range got {
		if got[i] != want[i] {
			t.Errorf("Got %v, want %v", got, want)
		}
	}
}

type QuadraticTestValues struct {
	time     int
	distance int
	wantMin  int
	wantMax  int
}

func TestQuadratic(t *testing.T) {
	inputs := []QuadraticTestValues{
		{7, 9, 2, 5},
		{15, 40, 4, 11},
		{30, 200, 11, 19},
	}
	for i := range inputs {
		gotMin, gotMax := quadratic(inputs[i].time, inputs[i].distance)
		if gotMin != inputs[i].wantMin || gotMax != inputs[i].wantMax {
			t.Errorf("Got %v %v, wanted %v %v", gotMin, gotMax, inputs[i].wantMin, inputs[i].wantMax)
		}
	}
}

func TestSolveA(t *testing.T) {
	races := parseInput(string(example))
	got := solveA(races)
	want := 288
	if got != want {
		t.Errorf("Got %v, want%v", got, want)
	}
}
