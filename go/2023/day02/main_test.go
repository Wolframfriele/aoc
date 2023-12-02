package main

import (
	"testing"
)

func TestParseInput(t *testing.T) {
	// want := []Game{
	// 	{
	// 		id: 1,
	// 		selections: []Selection{
	// 			{green: 0, blue: 3, red: 4},
	// 			{green: 2, blue: 6, red: 1},
	// 			{green: 2, blue: 0, red: 0},
	// 		},
	// 	},
	// 	{
	// 		id: 2,
	// 		selections: []Selection{
	// 			{green: 2, blue: 1, red: 0},
	// 			{green: 2, blue: 6, red: 1},
	// 			{green: 2, blue: 0, red: 0},
	// 		},
	// 	},
	// }

	input := `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue`
	got := parseInput(input)
	for i, game := range got {
		if game.id != i+1 {
			t.Errorf("Error parsing game.id got %q, wanted %q", game.id, i+1)
		}
	}
	firstSelection := Selection{green: 0, blue: 3, red: 4}
	if got[0].selections[0] != firstSelection {
		t.Errorf("Error parsing selections, got %v, wanted %v", got[0].selections[0], firstSelection)
	}
}

func TestSolveA(t *testing.T) {
	input := `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2and blue, 1 red, 2 green`
	parsedInput := parseInput(input)
	got := solveA(parsedInput, Selection{red: 12, green: 13, blue: 14})
	want := 8

	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}
