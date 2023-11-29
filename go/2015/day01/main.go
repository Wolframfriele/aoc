package main

import (
	"fmt"
	"os"
)

func solveA(input string)int32{
    var floor int32
    for _, char := range input{
        if char == '('{
            floor ++
        } else if char == ')' {
            floor --
        }
    }
    return floor
}

func solveB(input string)int32{
    var floor int32
    for pos, char := range input{
        if char == '('{
            floor ++
        } else if char == ')' {
            floor --
        }
        if floor == -1{
            return int32(pos) + 1
        }
    }
    return 0
}

func main(){
    input, err := os.ReadFile("2015/day01/input.txt")
    if err != nil {
        panic(err)
    }
    var resultA = solveA(string(input))
    fmt.Println(resultA)

    var resultB = solveB(string(input))
    fmt.Println(resultB)
}
