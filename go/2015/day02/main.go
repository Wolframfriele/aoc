package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func calcWrappingPaper(lengths []int) int {
	//* 2*l*w + 2*w*h + 2*h*l
	// + smallest side
	sort.Ints(lengths)
	return 3*(lengths[0]*lengths[1]) + 2*(lengths[0]*lengths[2]) + 2*(lengths[1]*lengths[2])
}

func solveA(input string) int {
	var total_paper int
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		split_line := strings.Split(line, "x")

		ints := make([]int, len(split_line))

		for i, s := range split_line {
			ints[i], _ = strconv.Atoi(s)
		}
		total_paper += calcWrappingPaper(ints)
	}
	return total_paper
}

func solveB(input string) int {
}

func main() {
	input, err := os.ReadFile("2015/day02/input.txt")
	if err != nil {
		panic(err)
	}
	result := solveA(string(input))
	fmt.Println(result)
}
