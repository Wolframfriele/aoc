package main

import (
	"fmt"
	"os"
	"slices"
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
	c.end = numList[1] + numList[2] - 1
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
	// for _, convPath := range conversionCollection {
	// 	fmt.Println(convPath)
	// }
	return
}

func convertInput(input int, conversonCollection []ConversionPath) int {
	for _, converter := range conversonCollection {
		if input >= converter.start && input <= converter.end {
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

func convertToRange(seeds []int) (ranges [][]int) {
	var pair []int
	for i := range seeds {
		if i%2 == 0 {
			pair = []int{}
			pair = append(pair, seeds[i])
		} else {
			pair = append(pair, seeds[i-1]+seeds[i]-1)
			slices.Sort(pair)
			ranges = append(ranges, pair)
		}
	}
	return
}

func inPath(num int, path ConversionPath) bool {
	if num >= path.start && num <= path.end {
		return true
	}
	return false
}

func convertRange(ranges [][]int, conversionMap []ConversionPath) (convRanges [][]int) {
	// fmt.Println(ranges)
	// fmt.Println("")
	// fmt.Println(conversionMap)
	for _, numRange := range ranges {
		// check if range overlaps with some of the conversionPaths
		foundOverlap := false
		for _, path := range conversionMap {
			if inPath(numRange[0], path) && inPath(numRange[1], path) {
				foundOverlap = true
				// fmt.Printf("Start %v + End %v within range: %v \n", numRange[0], numRange[1], path)
				convRanges = append(convRanges, []int{
					numRange[0] - path.difference,
					numRange[1] - path.difference,
				})
			} else if !inPath(numRange[0], path) && inPath(numRange[1], path) {
				// first number up to range start
				foundOverlap = true
				// fmt.Printf("Start %v not in range, End %v within range: %v \n", numRange[0], numRange[1], path)
				convRanges = append(convRanges, []int{
					numRange[0],
					path.start - 1,
				})
				// range start up to end number
				convRanges = append(convRanges, []int{
					path.start - path.difference,
					numRange[1] - path.difference,
				})
			} else if inPath(numRange[0], path) && !inPath(numRange[1], path) {
				// first number converted up to end range

				foundOverlap = true
				// fmt.Printf("Start %v in range, End %v not in range: %v \n", numRange[0], numRange[1], path)
				convRanges = append(convRanges, []int{
					numRange[0] - path.difference,
					path.end - path.difference,
				})
				// range end + 1
				convRanges = append(convRanges, []int{
					path.end + 1,
					numRange[1],
				})
			}
		}
		if !foundOverlap {
			// fmt.Printf("Start %v + End %v not in any range \n", numRange[0], numRange[1])
			convRanges = append(convRanges, []int{
				numRange[0],
				numRange[1],
			})
		}
		// fmt.Printf("Output ranges: %v\n", convRanges)
	}
	return
}

func solveB(seeds []int, maps [][]ConversionPath) (closest int) {
	inputRanges := convertToRange(seeds)
	fmt.Println(inputRanges)
	fmt.Println("")

	var outputRanges [][]int
	for _, conversionMap := range maps {
		fmt.Println(conversionMap)
		fmt.Println("")
		outputRanges = convertRange(inputRanges, conversionMap)
		// fmt.Println(outputRanges)
		// fmt.Println("")
		inputRanges = outputRanges
		outputRanges = [][]int{}
	}
	closest = inputRanges[0][0]
	for _, resultRange := range inputRanges {
		if resultRange[0] < closest {
			closest = resultRange[0]
		}
	}
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
