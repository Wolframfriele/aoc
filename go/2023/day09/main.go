package main

import (
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"
)

func parseInput(input string) (numSequences [][]int) {
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		var numSeq []int
		strSeq := strings.Fields(line)
		for _, strNum := range strSeq {
			num, err := strconv.Atoi(strNum)
			if err != nil {
				panic(err)
			}
			numSeq = append(numSeq, num)
		}
		numSequences = append(numSequences, numSeq)
	}
	return
}

func diff(numSeq []int) (diffSeq []int) {
	prev := numSeq[0]
	for i := 1; i < len(numSeq); i++ {
		diff := numSeq[i] - prev
		diffSeq = append(diffSeq, diff)
		prev = numSeq[i]
	}
	return
}

func notAllZero(seq []int) bool {
	for _, val := range seq {
		if val != 0 {
			return true
		}
	}
	return false
}

func predNext(numSeq []int) (next int) {
	differences := [][]int{numSeq}
	seq := numSeq
	for notAllZero(seq) {
		seq = diff(seq)
		differences = append(differences, seq)
	}
	for i := len(differences) - 2; i > -1; i-- {
		next = differences[i][len(differences[i])-1] + differences[i+1][len(differences[i+1])-1]
		differences[i] = append(differences[i], next)
	}
	return
}

func solveA(numSequences [][]int) (sum int) {
	for _, seq := range numSequences {
		sum += predNext(seq)
	}
	return
}

func reverse(s interface{}) {
	n := reflect.ValueOf(s).Len()
	swap := reflect.Swapper(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		swap(i, j)
	}
}

func solveB(numSequences [][]int) (sum int) {
	for _, seq := range numSequences {
		reverse(seq)
		sum += predNext(seq)
	}
	return
}

func main() {
	input, err := os.ReadFile("2023/day09/input.txt")
	if err != nil {
		panic(err)
	}
	numSequences := parseInput(string(input))
	resultA := solveA(numSequences)
	fmt.Printf("Result A: %v\n", resultA)

	resultB := solveB(numSequences)
	fmt.Printf("Result B: %v\n", resultB)
}
