package main

import (
	"testing"
)

// func TestParseConversionMap(t *testing.T) {
// 	mapStr := `seed-to-soil map:
// 50 98 2
// 52 50 48`
// 	got := parseConversionMap(mapStr)
// 	want := []ConversionPath{
// 		{50, 98, 2},
// 		{52, 50, 48},
// 	}
// 	for i := range got {
// 		if got[i].dest != want[i].dest ||
// 			got[i].source != want[i].source ||
// 			got[i].difference != want[i].rangeLen {
// 			t.Errorf("got %v, wanted %v", got[i], want[i])
// 		}
// 	}
// }

func TestParseConversionMap(t *testing.T) {
	mapStr := `seed-to-soil map:
50 98 2
52 50 48`
	got := parseConversionMap(mapStr)
	want := []ConversionPath{
		{98, 100, 48},
		{50, 98, -2},
	}
	for i := range got {
		if got[i].start != want[i].start ||
			got[i].end != want[i].end ||
			got[i].difference != want[i].difference {
			t.Errorf("got %v, wanted %v", got[i], want[i])
		}
	}
}

func TestConvertInput(t *testing.T) {
	converter := []ConversionPath{
		{98, 100, 48},
		{50, 98, -2},
	}
	got := convertInput(79, converter)
	want := 81
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

const exampleInput = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`

func TestParseInput(t *testing.T) {
	seedsGot, collectionGot := parseInput(string(exampleInput))
	seedsWant := []int{79, 14, 55, 13}
	for i := range seedsGot {
		if seedsGot[i] != seedsWant[i] {
			t.Errorf("got %v, wanted %v", seedsGot[i], seedsWant[i])
		}
	}
	collectionWant := [][]ConversionPath{
		{
			{98, 100, 48},
			{50, 98, -2},
		},
	}
	for i := range collectionWant[0] {
		if collectionGot[0][i] != collectionWant[0][i] {
			t.Errorf("got %v, wanted %v", collectionGot[0][i], collectionWant[0][i])
		}
	}
}

func TestSolveA(t *testing.T) {
	seeds, maps := parseInput(string(exampleInput))
	got := solveA(seeds, maps)
	want := 35

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

func TestSolveB(t *testing.T) {
	seeds, maps := parseInput(string(exampleInput))
	got := solveB(seeds, maps)
	want := 46

	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}
