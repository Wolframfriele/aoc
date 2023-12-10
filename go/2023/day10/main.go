package main

import (
	"fmt"
	"os"
	"strings"
)

var convertSymbols = map[rune][]Coordinate{
	'|': {{0, -1}, {0, 1}},
	'-': {{-1, 0}, {1, 0}},
	'L': {{0, -1}, {1, 0}},
	'J': {{-1, 0}, {0, -1}},
	'7': {{-1, 0}, {0, 1}},
	'F': {{1, 0}, {0, 1}},
}

var aroundCoor = []Coordinate{
	{0, -1}, {1, 0}, {0, 1}, {-1, 0},
}

type Coordinate struct {
	x int
	y int
}

func (c Coordinate) Add(coor Coordinate) Coordinate {
	newCoor := c
	newCoor.x = c.x + coor.x
	newCoor.y = c.y + coor.y
	return newCoor
}

type PipeSystem struct {
	graph map[Coordinate][]Coordinate
	start Coordinate
}

func (p *PipeSystem) ParseInput(input string) {
	lines := strings.Split(input, "\n")
	p.graph = make(map[Coordinate][]Coordinate)
	for y := range lines {
		if len(lines[y]) == 0 {
			continue
		}
		for x, char := range lines[y] {
			c := Coordinate{x, y}
			if char != 'S' && char != '.' {
				for _, coor := range convertSymbols[rune(char)] {
					p.graph[c] = append(p.graph[c], c.Add(coor))
				}
			} else if char == 'S' {
				p.start = Coordinate{x, y}
			}
		}
	}
}

func findFirst(p *PipeSystem) (firstCoor Coordinate) {
	for _, coor := range aroundCoor {
		checkedCoor := p.start.Add(coor)
		neigbors := p.graph[checkedCoor]
		if len(neigbors) != 2 {
			continue
		}
		if neigbors[0] == p.start || neigbors[1] == p.start {
			firstCoor = checkedCoor
			return
		}
	}
	return
}

func solveA(p *PipeSystem) (dist int) {
	dist += 1
	previous := p.start
	current := findFirst(p)

	for current != p.start {
		nextNodes := p.graph[current]
		for _, coor := range nextNodes {
			if coor != previous {
				previous = current
				current = coor
				dist += 1
				break
			}
		}
	}

	return dist / 2
}

// func solveB(numSequences [][]int) (sum int) {
// 	for _, seq := range numSequences {
// 		reverse(seq)
// 		sum += predNext(seq)
// 	}
// 	return
// }

func main() {
	input, err := os.ReadFile("2023/day10/input.txt")
	if err != nil {
		panic(err)
	}
	pipes := PipeSystem{}
	pipes.ParseInput(string(input))
	resultA := solveA(&pipes)
	fmt.Printf("Result A: %v\n", resultA)

	// resultB := solveB(graph)
	// fmt.Printf("Result B: %v\n", resultB)
}
