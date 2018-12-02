#! /usr/bin/env python3
# Day 1 - Puzzle 1
# Calculate resulting frequency after all changes applied


def total_freq(input_file):
    total = 0

    with open(input_file) as file:
        for line in file:
            total += int(line.strip())

    return total


print(total_freq('./day01-input.txt'))
