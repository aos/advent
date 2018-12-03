# Day 3 - Puzzle 1
# How many square inches of fabric are within two or more claims?

import re


w, h = 1000, 1000
FABRIC = [[0 for x in range(w)] for y in range(h)]


def intersecting(fabric):
    claims = 0
    for col in fabric:
        for row in col:
            if row > 1:
                claims += 1

    return claims


def populate(query, fabric):
    claim_id, start_point, dimensions = \
        re.match(r'^(#\d+)\D+(\d+,\d+)\D+(\d+x\d+)$', query).groups()

    x, y = [int(i) for i in start_point.split(',')]
    width, height = [int(i) for i in dimensions.split('x')]

    for i in range(y, y+height):
        for j in range(x, x+width):
            fabric[i][j] += 1


with open('./day03-input.txt') as f:
    for line in f:
        populate(line, FABRIC)

    res = intersecting(FABRIC)
    print(res)

test_input = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]
TEST_FABRIC = [[0 for x in range(8)] for y in range(8)]
for i in test_input:
    populate(i, TEST_FABRIC)
intersecting(TEST_FABRIC)
