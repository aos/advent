# Day 23 - Part 1
# Find the nanobot with the largest signal radius. How many nanobots are in
# range of its signal?


import re


def manh_d(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def parse_line(line):
    return tuple(map(int, re.findall(r'-?\d+', line)))


def parse_input(file):
    return [parse_line(line.strip()) for line in open(file).readlines()]


def solve(file):
    inp = parse_input(file)
    largest_range = -float('inf')
    largest_bot = None
    total = 0

    for index, bot in enumerate(inp):
        if bot[3] > largest_range:
            largest_bot = bot
            largest_range = bot[3]

    for bot in inp:
        d = manh_d((bot[0], bot[1], bot[2]),
                   (largest_bot[0], largest_bot[1], largest_bot[2]))
        if d <= largest_range:
            total += 1

    return total


if __name__ == '__main__':
    # Tests
    nano1 = (0, 0, 0)
    nano2 = (1, 1, 2)
    test_line = 'pos=<-1324,341,3401>, r=5'
    assert manh_d(nano1, nano2) == 4
    assert parse_line(test_line) == (-1324, 341, 3401, 5)
    assert solve('./example-input.txt') == 7
    print('All tests passed!')

    # Solution
    print(solve('./day23-input.txt'))
