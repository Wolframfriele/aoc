package main

import "testing"

func TestFindDigits(t *testing.T) {
	got := findDigits("a2bcd3ds4c")
	want := 24

	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}
