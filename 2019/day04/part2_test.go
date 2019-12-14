package main

import "testing"

func TestPartTwo(t *testing.T) {
	tests := []struct {
		num           int
		meetsCriteria bool
	}{
		{223450, false},
		{123789, false},
		{111122, true},
		{112233, true},
		{123444, false},
		{111111, false},
		{113444, true},
	}

	for _, tt := range tests {
		res := PartTwo(tt.num)
		if res != tt.meetsCriteria {
			t.Errorf("Test: %d, Want: %t, Got: %t",
				tt.num, tt.meetsCriteria, res)
		}
	}
}
