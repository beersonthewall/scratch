package main

import (
	"calc/calc"
	"flag"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var op string
	flag.StringVar(&op, "op", "", "Command to execute. One of: add, sub, mul, div")
	flag.Parse()

	args := flag.Args()
	numbers := make([]float64, 0, len(args))
	for _, maybeNum := range args {
		i, err := strconv.ParseFloat(maybeNum, 64)
		if err != nil {
			fmt.Println(maybeNum, " is not a number")
			os.Exit(1)
		}
		numbers = append(numbers, i)
	}

	switch op {
	case calc.CmdSum:
		fmt.Println(calc.Sum(&numbers))
	case calc.CmdProduct:
		fmt.Println(calc.Product(&numbers))
	case calc.CmdMean:
		fmt.Println(calc.Mean(&numbers))
	case calc.CmdSqrt:
		calc.Sqrt(&numbers)
		fmt.Println(numbers)
	default:
		panic(fmt.Sprintf("Invalid operation: %s", op))
	}
}
