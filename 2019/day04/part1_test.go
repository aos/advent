package main

import "testing"

func TestPartOne(t *testing.T) {
	tests := []struct {
		num           int
		meetsCriteria bool
	}{
		{111111, true},
		{223450, false},
		{123789, false},
	}

	for _, tt := range tests {
		res := PartOne(tt.num)
		if res != tt.meetsCriteria {
			t.Fatalf("Want: %t, Got: %t", tt.meetsCriteria, res)
		}
	}
}
