package main

import (
	"fmt"
	"os"
	"strings"
)

func parseInput(input string) (directions string, graph map[string][]string) {
	inputs := strings.Split(input, "\n\n")
	directions = inputs[0]
	graphLines := strings.Split(inputs[1], "\n")
	graph = make(map[string][]string)
	for _, line := range graphLines {
		if len(line) == 0 {
			continue
		}
		graphParts := strings.Split(line, " = ")
		nodes := strings.Split(strings.Trim(graphParts[1], "()"), ", ")
		graph[graphParts[0]] = nodes
	}
	return
}

func solveA(directions string, graph map[string][]string) (steps int) {
	dirLen := len(directions)
	currentNode := "AAA"

	for i := 0; currentNode != "ZZZ"; i++ {
		currentDir := rune(directions[i%dirLen])
		if currentDir == 'L' {
			currentNode = graph[currentNode][0]
		} else {
			currentNode = graph[currentNode][1]
		}
		steps++
	}
	return
}

func traverse(start string, directions string, graph map[string][]string) (steps int) {
	dirLen := len(directions)
	currentNode := start

	for i := 0; rune(currentNode[2]) != 'Z'; i++ {
		currentDir := rune(directions[i%dirLen])
		if currentDir == 'L' {
			currentNode = graph[currentNode][0]
		} else {
			currentNode = graph[currentNode][1]
		}
		steps++
	}
	return
}

func primeFactors(num int) (factors map[int]int) {
	factors = make(map[int]int)
	lastFactor, lastRemainder := 0, num
	for i := num; lastRemainder > 1; i = lastRemainder {
		lastFactor, lastRemainder = factor(i)
		factors[lastFactor]++
	}
	return
}

func factor(num int) (factor int, remainder int) {
	for i := 2; i <= num; i++ {
		if num%i == 0 {
			factor = i
			remainder = num / i
			break
		}
	}
	return
}

func pow(base, exponent int) int {
	result := 1
	for i := 1; i <= exponent; i++ {
		result *= base
	}
	return result
}

func findLeastCommonMultiple(nums []int) (lcm int) {
	commonFactors := make(map[int]int)
	for _, num := range nums {
		factors := primeFactors(num)
		for fac, count := range factors {
			if commonFactors[fac] < count {
				commonFactors[fac] = count
			}
		}
	}
	lcm = 1
	fmt.Println(commonFactors)
	for fac, count := range commonFactors {
		lcm *= pow(fac, count)
	}
	return
}

func solveB(directions string, graph map[string][]string) (steps int) {
	var frequencyCount []int
	for node := range graph {
		if rune(node[2]) != 'A' {
			continue
		}
		frequencyCount = append(frequencyCount, traverse(node, directions, graph))
	}
	fmt.Println(frequencyCount)
	steps = findLeastCommonMultiple(frequencyCount)
	return
}

func main() {
	input, err := os.ReadFile("2023/day08/input.txt")
	if err != nil {
		panic(err)
	}
	directions, graph := parseInput(string(input))
	resultA := solveA(directions, graph)
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(directions, graph)
	fmt.Printf("Result B: %v\n", resultB)
}
