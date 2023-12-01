package main

import (
	"testing"
)

type getNumberTest struct {
	input    string
	i        int
	expected rune
}

var getNumberTests = []getNumberTest{
	{"2", 0, '2'},
	{"a5", 1, '5'},
	{"a5", 0, ' '},
	{"one", 0, '1'},
	{"two", 0, '2'},
	{"three", 0, '3'},
	{"four", 0, '4'},
	{"totwo", 2, '2'},
}

func TestGetNumber(t *testing.T) {
	for _, test := range getNumberTests {
		output := getNumber(test.input, test.i, true)
		if output != test.expected {
			t.Errorf("Got: %q, wanted: %q, for inputs (%q, %v)", output, test.expected, test.input, test.i)
		}
	}
}

func TestSolveA(t *testing.T) {
	input := `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`
	got := solveB(input)
	want := 142

	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}

func TestSolveB(t *testing.T) {
	input := `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
	got := solveB(input)
	want := 281

	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}

func TestFindDigits(t *testing.T) {
	got := findDigits("a2bcd3ds4c", false)
	want := 24

	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}
