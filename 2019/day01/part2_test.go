package main

import (
	"strings"
	"testing"
)

func TestPartTwo(t *testing.T) {
	examples := []struct {
		mass string
		fuel int
	}{
		{"14\n1969", 2 + 966},
		{"100756", 50346},
		{"118602", 59270},
		{"1969", 966},
	}

	for _, tt := range examples {
		res := PartTwo(strings.NewReader(tt.mass))
		if res != tt.fuel {
			t.Fatalf("Wanted: %d, Got: %d", tt.fuel, res)
		}
	}
}
