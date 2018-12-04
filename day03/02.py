# Day 3 - Puzzle 2
# ID of the only claim that does not overlap

import re
import collections


def build_fabric(w, h):
    return [[[] for x in range(w)] for y in range(h)]


def populate(query, claims, fabric):
    claim_id, start_point, dimensions = \
        re.match(r'^(#\d+)\D+(\d+,\d+)\D+(\d+x\d+)$', query).groups()

    claims[claim_id] = True

    x, y = [int(i) for i in start_point.split(',')]
    width, height = [int(i) for i in dimensions.split('x')]

    for i in range(y, y+height):
        for j in range(x, x+width):
            fabric[i][j].append(claim_id)

            if len(fabric[i][j]) > 1:
                for cl in fabric[i][j]:
                    claims[cl] = False


def find_non_overlap(claims):
    return next(k for k, v in claims.items() if v)


with open('./day03-input.txt') as f:
    cs = collections.defaultdict(bool)
    FABRIC = build_fabric(1000, 1000)

    for line in f:
        populate(line.strip(), cs, FABRIC)

    res = find_non_overlap(cs)
    print(res)

# Tests
test_input = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]
TEST_FABRIC = build_fabric(8, 8)
cs = collections.defaultdict(bool)
for i in test_input:
    populate(i, cs, TEST_FABRIC)
assert(find_non_overlap(cs) == '#3')
print('All tests passed!')
