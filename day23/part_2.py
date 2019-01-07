# Day 23 - Part 2
# What is the shortest manhattan distance between any of those points and
# 0,0,0?


from part_1 import parse_input
from collections import defaultdict


def solve(file):
    points = defaultdict(int)
    inp = parse_input(file)

    for x, y, z, r in inp:
        s = x + y + z
        low, high = (s - r, s + r)

        points[low] += 1
        points[high] += 1

    return max(points.keys(), key=(lambda k: points[k]))


# Test
assert solve('./example2.txt') == 36
print('All tests passed!')

# Solution
print(solve('./day23-input.txt'))
