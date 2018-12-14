# Day 13 - Puzzle 1
# What is the location of the first crash?


from pprint import pprint
import collections


def run(file):
    steps = 0
    layout = _create_layout(file)
    locations = _store_carts(layout)

    # Go on forever... or until a crash happens
    while steps < 1:
        for y, row in enumerate(layout):
            cart = ''
            prev_tile = ''
            for x, cell in enumerate(row):
                loc = '{},{}'.format(x, y)
                if cell == '-' or cell == '|' or cell == '\\' or cell == '/':
                    if cart:
                        layout[y][x] = cart
                        cart = ''
                    else:
                        prev_tile = cell

                else:
                    d, new_x, new_y = _find_coords(layout, cell, x, y)
                    next_step = layout[new_y][new_x]
                    new_loc = '{},{}'.format(new_x, new_y)

                    if next_step == '+':
                        pass
                    else:
                        new_d = _step_forward(layout, d, new_x, new_y)
                        cart = new_d
                        layout[y][x] = prev_tile

                        # Crash detected
                        if new_loc in locations:
                            return new_x, new_y
                        locations[new_loc] = locations[loc]
                        del locations[loc]

        steps += 1

    return layout


def _step_forward(layout, direction, x, y):
    steps = {
        '-': {
            '+': '>',
            '-': '<'
        },
        '|': {
            '+': '^',
            '-': 'v'
        },
        '\\': {
            '>': 'v',
            '^': '<',
            '<': '^',
            'v': '>'
        },
        '/': {
            '>': '^',
            '^': '>',
            '<': 'v',
            'v': '<'
        }
    }
    next_step = layout[y][x]
    return steps[next_step][direction]


def _find_coords(layout, d, x, y):
    direction = ''
    if d == '>':
        x += 1
        direction = '+'
    elif d == '<':
        x -= 1
        direction = '-'
    elif d == 'v':
        y += 1
        direction = '+'
    else:
        y -= 1
        direction = '-'

    return direction, x, y


def _store_carts(grid):
    store = collections.defaultdict(int)
    carts = ['>', '<', 'v', '^']

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in carts:
                store['{},{}'.format(x, y)] = 0

    return store


def _create_layout(file):
    grid = []
    with open(file) as f:
        for line in f:
            row = []
            row.extend([i for i in line.strip('\n')])
            grid.append(row)

    return grid


# Tests
TEST_LAYOUT = _create_layout('./example-in.txt')
TEST_STORE = _store_carts(TEST_LAYOUT)
assert(TEST_STORE == {'2,0': 0, '9,3': 0})
print('All tests passed!')

print(run('./example-in.txt'))
