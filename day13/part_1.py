# Day 13 - Puzzle 1
# What is the location of the first crash?

from enum import Enum
from pprint import pprint
import collections


class CartKind(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'


class TrackKind(Enum):
    NS = '|'
    EW = '-'
    NE_SW = '\\'
    NW_SE = '/'
    XROADS = '+'


def _tick(carts, grid):
    while True:
        carts = sorted(carts, key=lambda x: x['location'])
        for cart in carts:
            cart_x, cart_y = cart['location']
            cart_type = cart['type']
            cart_dir = cart['direction']

            if cart_type == CartKind.LEFT:
                cart_x -= 1
            elif cart_type == CartKind.RIGHT:
                cart_x -= 1
            elif cart_type == CartKind.UP:
                cart_y -= 1
            elif cart_type == CartKind.DOWN:
                cart_y += 1

            cart['location'] = (cart_x, cart_y)


def _create_state(file):
    carts = []
    grid = []
    with open(file) as f:
        for line in f:
            row = []
            row.extend([i for i in line.strip('\n')])
            grid.append(row)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in '^v<>':
                if (
                    CartKind(cell) == CartKind.UP or
                    CartKind(cell) == CartKind.DOWN
                ):
                    grid[y][x] = TrackKind.NS
                elif (
                    CartKind(cell) == CartKind.LEFT or
                    CartKind(cell) == CartKind.RIGHT
                ):
                    grid[y][x] = TrackKind.EW

                cart_state = {
                    'location': (x, y),
                    'type': CartKind(cell),
                    'direction': 0
                }
                carts.append(cart_state)
            elif cell in '|-\\/+':
                grid[y][x] = TrackKind(cell)

    return carts, grid


# Tests
TEST_CARTS, TEST_GRID = _create_state('./example-in.txt')
assert(TEST_CARTS == [
    {'location': (2, 0), 'type': CartKind.RIGHT, 'direction': 0},
    {'location': (9, 3), 'type': CartKind.DOWN, 'direction': 0}
])
print(_sort_carts(TEST_CARTS))
print('All tests passed!')
