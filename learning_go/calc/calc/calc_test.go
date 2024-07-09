package calc

import (
	"math"
	"testing"
)

func TestSumEmpty(t *testing.T) {
	var empty []float64
	result := Sum(&empty)
	if result != 0 {
		t.Fatalf("Sum returned nonzero result: %f for empty slice", result)
	}
}

func TestSum(t *testing.T) {
	nums := []float64{1.0, 2.4, -0.4}
	result := Sum(&nums)
	if math.Abs(3.0-result) > .01 {
		t.Fatalf("Result %f of summing %f not within bound of 0.01", result, nums)
	}
}

func TestProductEmpty(t *testing.T) {
	var empty []float64
	result := Product(&empty)
	if result != 1 {
		t.Fatalf("Product returned result != 1 for empty list")
	}
}

func TestProduct(t *testing.T) {
	nums := []float64{1.0, 2.4, -0.4}
	result := Product(&nums)
	if math.Abs(-0.96-result) > .01 {
		t.Fatalf("Result %f of multiplying %f not within bound of 0.01", result, nums)
	}
}

func TestMeanEmpty(t *testing.T) {
	var empty []float64
	result := Mean(&empty)
	if result != 0 {
		t.Fatalf("Mean returned result %f for empty list", result)
	}
}

func TestMean(t *testing.T) {
	nums := []float64{1.0, 2.4, -0.4}
	result := Mean(&nums)
	if math.Abs(1-result) > .01 {
		t.Fatalf("Mean %f not within bound of 0.01", result)
	}
}

func TestSqrtEmpty(t *testing.T) {
	var empty []float64
	Sqrt(&empty)
	if len(empty) != 0 {
		t.Fatalf("Sqrt on empty slice non-empty result: %f", empty)
	}
}

func TestSqrt(t *testing.T) {
	nums := []float64{1.0, 2.4, -0.4}
	e := []float64{1.0, 1.549, -0.4}
	Sqrt(&nums)
	for i := 0; i < len(nums); i += 1 {
		if math.Abs(nums[i]-e[i]) >= 0.1 {
			t.Fatalf("Sqrt: %f not near enough to %f", nums[i], e[i])
		}
	}
}
