#!/usr/bin/env python3
# Day 1 - Puzzle 2
# First frequency the device reaches twice


def duplicate_freq(input_file):
    dups = set()
    freq = 0

    while True:
        with open(input_file) as file:
            for line in file:
                freq += int(line.strip())

                if freq in dups:
                    return freq

                dups.add(freq)


print(duplicate_freq('./day01-input.txt'))
