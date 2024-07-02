package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
)

const (
	Add string = "add"
	Sub string = "sub"
	Mul string = "mul"
	Div string = "div"
)

func mathOp(op *string) func(int64, int64) (int64) {
	var f func(int64, int64) (int64)
	switch *op {
	case Add:
		f = func(a int64, b int64) int64 {
			return a + b
		}
	case Sub:
		f = func(a int64, b int64) int64 {
			return a - b
		}
	case Mul:
		f = func(a int64, b int64) int64 {
			return a * b
		}
	case Div:
		f = func(a int64, b int64) int64 {
			if b == 0 {
				fmt.Println("Attempted to divide by zero!")
				os.Exit(1)
			}
			return a / b
		}
	default:
		fmt.Println("Invalid operation ", op)
		os.Exit(1)
	}
	return f
}

func main() {
	var op string
	flag.StringVar(&op, "op", "", "Command to execute. One of: add, sub, mul, div")
	flag.Parse()

	f := mathOp(&op)

	args := flag.Args()
	numbers := make([]int64, 0, len(args))
	for _, maybeNum := range args {
		i, err := strconv.ParseInt(maybeNum, 10, 64)
		if err != nil {
			fmt.Println(maybeNum, " is not a number")
			os.Exit(1)
		}
		numbers = append(numbers, i)
	}

	var acc int64 = 0
	for _, num := range numbers {
		acc = f(acc, num)
	}
	fmt.Println(acc)
}
