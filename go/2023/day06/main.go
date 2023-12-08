package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// Time:      7  15   30
// Distance:  9  40  200

type Race struct {
	time     int
	distance int
}

func parseInputA(input string) (races []Race) {
	lines := strings.Split(input, "\n")
	times := strings.Fields(lines[0])
	distances := strings.Fields(lines[1])
	for i := range times {
		if i > 0 {
			time, _ := strconv.Atoi(times[i])
			distance, _ := strconv.Atoi(distances[i])
			races = append(races, Race{time, distance})
		}
	}
	return
}

func parseInputB(input string) (races []Race) {
	lines := strings.Split(input, "\n")
	times := strings.Split(lines[0], ":")
	distances := strings.Split(lines[1], ":")
	timeStr := strings.ReplaceAll(times[1], " ", "")
	distStr := strings.ReplaceAll(distances[1], " ", "")

	time, _ := strconv.Atoi(timeStr)
	distance, _ := strconv.Atoi(distStr)
	races = append(races, Race{time, distance})
	return
}

// for every millisecond holding button
//  boat speed increases one millimeter per millisecond

// Maximize distance traveled in maximum distance traveled

// distance_travelled = time_left * max speed

// (total_time - time_charging) * time_charging > record_distance

// for each race find the number of ways to beat the record
// Multiply the max amount of solutions per race

func quadratic(time int, dist int) (min, max int) {
	timeFl := float64(time)
	distFl := float64(dist)
	min = int(math.Ceil(((-timeFl + math.Sqrt(timeFl*timeFl-4*distFl)) / -2) + .001))
	max = int(math.Floor(((-timeFl - math.Sqrt(timeFl*timeFl-4*distFl)) / -2) - 0.001))
	return
}

func solveA(races []Race) (prod int) {
	prod = 1
	for _, race := range races {
		min, max := quadratic(race.time, race.distance)
		posibilities := max - min + 1
		prod *= posibilities
	}
	return
}

func main() {
	input, err := os.ReadFile("2023/day06/input.txt")
	if err != nil {
		panic(err)
	}
	races := parseInputA(string(input))
	resultA := solveA(races)
	fmt.Printf("Result A: %v\n", resultA)

	racesB := parseInputB(string(input))
	resultB := solveA(racesB)
	fmt.Printf("Result B: %v\n", resultB)
}
