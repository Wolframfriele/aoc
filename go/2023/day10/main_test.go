package main

import (
	"testing"
)

const example = `-L|F7
7S-7|
L|7||
-L-J|
L|-JF
`

const example2 = `7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
`

func TestSolveA(t *testing.T) {
	pipes := PipeSystem{}
	pipes.ParseInput(example)
	result := solveA(&pipes)
	want := 4
	if result != want {
		t.Errorf("Got %v, wanted %v", result, want)
	}

	pipes2 := PipeSystem{}
	pipes2.ParseInput(example2)
	result2 := solveA(&pipes2)
	want2 := 8
	if result2 != want2 {
		t.Errorf("Got %v, wanted %v", result2, want2)
	}
}
