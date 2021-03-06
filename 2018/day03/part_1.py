# Day 3 - Puzzle 1
# How many square inches of fabric are within two or more claims?

import re


def _build_fabric(w, h):
    return [[0 for x in range(w)] for y in range(h)]


def split_query(q):
    return re.match(r'^(#\d+)\D+(\d+,\d+)\D+(\d+x\d+)$', q).groups()


def _populate(query, fabric):
    claim_id, start_point, dimensions = split_query(query)

    x, y = [int(i) for i in start_point.split(',')]
    width, height = [int(i) for i in dimensions.split('x')]

    for i in range(y, y+height):
        for j in range(x, x+width):
            fabric[i][j] += 1


def _intersecting(fabric):
    claims = 0
    for row in fabric:
        for cell in row:
            if cell > 1:
                claims += 1

    return claims


if __name__ == '__main__':
    with open('./day03-input.txt') as f:
        FABRIC = _build_fabric(1000, 1000)

        for line in f:
            _populate(line.strip(), FABRIC)

        res = _intersecting(FABRIC)
        print(res)

    # Test
    test_input = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]
    TEST_FABRIC = _build_fabric(8, 8)
    for i in test_input:
        _populate(i, TEST_FABRIC)
    assert(split_query(test_input[0]) == ('#1', '1,3', '4x4'))
    assert(_intersecting(TEST_FABRIC) == 4)
    print('All tests passed!')
