package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func calcWrappingPaperA(lengths []int) int {
	//* 2*l*w + 2*w*h + 2*h*l
	// + smallest side
	return 3*(lengths[0]*lengths[1]) + 2*(lengths[0]*lengths[2]) + 2*(lengths[1]*lengths[2])
}

func calcWrappingPaperB(lengths []int) int {
	// 2 * smalles + 2 * mid
	// + l * w * h for bow
	return (2 * lengths[0]) + (2 * lengths[1]) + (lengths[0] * lengths[1] * lengths[2])
}

func solve(input string) (paperSumA, paperSumB int) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		split_line := strings.Split(line, "x")

		ints := make([]int, len(split_line))

		for i, s := range split_line {
			ints[i], _ = strconv.Atoi(s)
		}
		sort.Ints(ints)
		paperSumA += calcWrappingPaperA(ints)
		paperSumB += calcWrappingPaperB(ints)
	}
	return
}

func main() {
	input, err := os.ReadFile("2015/day02/input.txt")
	if err != nil {
		panic(err)
	}
	resultA, resultB := solve(string(input))
	fmt.Println(resultA)
	fmt.Println(resultB)
}
