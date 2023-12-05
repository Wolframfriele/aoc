package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type ConversionPath struct {
	start      int
	end        int
	difference int
}

func (c *ConversionPath) FromString(input string) {
	numList := convertToIntSlice(input)
	c.start = numList[1]
	c.end = numList[1] + numList[2]
	c.difference = numList[1] - numList[0]
}

func convertToIntSlice(stringSlice string) (intSlice []int) {
	split := strings.Fields(stringSlice)
	for _, numStr := range split {
		num, err := strconv.Atoi(numStr)
		if err != nil {
			fmt.Printf("Coult not convert (%v) to integer\n", numStr)
		}
		intSlice = append(intSlice, num)
	}
	return
}

func parseConversionMap(input string) (conversionMap []ConversionPath) {
	lines := strings.Split(input, "\n")
	for _, line := range lines[1:] {
		newPath := new(ConversionPath)
		newPath.FromString(line)
		conversionMap = append(conversionMap, *newPath)
	}
	return
}

func parseInput(input string) (seeds []int, conversionCollection [][]ConversionPath) {
	lines := strings.Split(input, "\n\n")
	seeds = convertToIntSlice(lines[0][7:])
	for _, conversionMapStr := range lines[1:] {
		if len(conversionMapStr) > 0 {
			conversionCollection = append(conversionCollection, parseConversionMap(conversionMapStr))
		}
	}
	return
}

func convertInput(input int, conversonCollection []ConversionPath) int {
	for _, converter := range conversonCollection {
		if input >= converter.start && input < converter.end {
			return input - converter.difference
		}
	}
	return input
}

func min(input []int) (min int) {
	min = input[0]
	for _, val := range input {
		if val < min {
			min = val
		}
	}
	return
}

func solveA(seeds []int, maps [][]ConversionPath) (closest int) {
	var locations []int
	for _, seed := range seeds {
		converted := seed
		for i := range maps {
			converted = convertInput(converted, maps[i])
		}
		locations = append(locations, converted)
	}
	closest = min(locations)
	return
}

func solveB(seeds []int, maps [][]ConversionPath) (closest int) {
	var locations []int
	for i := range seeds {
		if i%2 == 0 {
			for j := seeds[i]; j < seeds[i]+seeds[i+1]; j++ {
				converted := j
				for id := range maps {
					converted = convertInput(converted, maps[id])
				}
				locations = append(locations, converted)
			}
		}
	}
	closest = min(locations)
	return
}

func main() {
	input, err := os.ReadFile("2023/day05/input.txt")
	if err != nil {
		panic(err)
	}
	seeds, collection := parseInput(string(input))
	resultA := solveA(seeds, collection)
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(seeds, collection)
	fmt.Printf("Result B: %v\n", resultB)
}
