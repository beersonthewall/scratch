package calc

import (
	"math"
)

const (
	CmdSum     string = "sum"
	CmdProduct string = "product"
	CmdMean    string = "mean"
	CmdSqrt    string = "sqrt"
)

func Sum(nums *[]float64) float64 {
	var s float64
	for _, n := range *nums {
		s += n
	}
	return s
}

func Product(nums *[]float64) float64 {
	var p float64 = 1
	for _, n := range *nums {
		p *= n
	}
	return p
}

func Mean(nums *[]float64) float64 {
	if len(*nums) == 0 {
		return 0
	}

	l := float64(len(*nums))
	s := Sum(nums)
	return s / l
}

func Sqrt(nums *[]float64) {
	for i := 0; i < len(*nums); i++ {
		if (*nums)[i] >= 0 {
			(*nums)[i] = math.Sqrt((*nums)[i])
		}
	}
}
