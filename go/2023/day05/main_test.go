package main

import (
	"testing"
)

func TestParseConversionMap(t *testing.T) {
	mapStr := `seed-to-soil map:
50 98 2
52 50 48`
	got := parseConversionMap(mapStr)
	want := []ConversionPath{
		{98, 99, 48},
		{50, 97, -2},
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

// no number in path
// in   [10, 15]
// conv {20, 25, 5}
// out  [[10, 15]]

type ConvertRangeTest struct {
	inputRanges   [][]int
	conversionMap []ConversionPath
	outputRange   [][]int
}

func TestConvertRange(t *testing.T) {
	tests := []ConvertRangeTest{
		{inputRanges: [][]int{{10, 15}}, conversionMap: []ConversionPath{{3, 20, -5}}, outputRange: [][]int{{15, 20}}},
		{inputRanges: [][]int{{10, 15}}, conversionMap: []ConversionPath{{12, 20, 2}}, outputRange: [][]int{{10, 11}, {10, 13}}},
		{inputRanges: [][]int{{10, 15}}, conversionMap: []ConversionPath{{5, 12, 2}}, outputRange: [][]int{{8, 10}, {13, 15}}},
		{inputRanges: [][]int{{10, 15}}, conversionMap: []ConversionPath{{20, 25, -5}}, outputRange: [][]int{{10, 15}}},
		{inputRanges: [][]int{{79, 92}, {55, 67}}, conversionMap: []ConversionPath{{98, 99, 48}, {50, 97, -2}}, outputRange: [][]int{{81, 94}, {57, 69}}},
		{inputRanges: [][]int{{79, 100}, {45, 67}}, conversionMap: []ConversionPath{{98, 99, 48}, {50, 97, -2}}, outputRange: [][]int{{81, 99}, {98, 100}, {45, 49}, {52, 69}}},
		{inputRanges: [][]int{{1, 50}}, conversionMap: []ConversionPath{{15, 20, -5}}, outputRange: [][]int{{1, 14}, {10, 15}, {21, 50}}},
	}
	for _, test := range tests {
		result := convertRange(test.inputRanges, test.conversionMap)
		for i := range result {
			for j := range result[i] {
				if result[i][j] != test.outputRange[i][j] {
					t.Errorf("Wanted %v, got %v", test.outputRange[i][j], result[i][j])
				}
			}
		}
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
			{98, 99, 48},
			{50, 97, -2},
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
