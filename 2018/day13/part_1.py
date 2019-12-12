# Day 13 - Puzzle 1
# What is the location of the first crash?

from enum import Enum


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
    XR = '+'


def _tick(carts, grid):
    types = {
        TrackKind.EW: {
            CartKind.RIGHT: CartKind.RIGHT,
            CartKind.LEFT: CartKind.LEFT
        },
        TrackKind.NS: {
            CartKind.UP: CartKind.UP,
            CartKind.DOWN: CartKind.DOWN
        },
        TrackKind.NE_SW: {
            CartKind.RIGHT: CartKind.DOWN,
            CartKind.UP: CartKind.LEFT,
            CartKind.LEFT: CartKind.UP,
            CartKind.DOWN: CartKind.RIGHT
        },
        TrackKind.NW_SE: {
            CartKind.RIGHT: CartKind.UP,
            CartKind.DOWN: CartKind.LEFT,
            CartKind.LEFT: CartKind.DOWN,
            CartKind.UP: CartKind.RIGHT
        }
    }
    xr_directions = [CartKind.UP, CartKind.RIGHT, CartKind.DOWN, CartKind.LEFT]
    steps = 0
    while True:
        carts = sorted(carts, key=lambda x: x['location'])
        for cart in carts:
            cart_x, cart_y = cart['location']
            cart_type = cart['type']
            cart_dir = cart['direction']

            if cart_type == CartKind.LEFT:
                cart_x -= 1
            elif cart_type == CartKind.RIGHT:
                cart_x += 1
            elif cart_type == CartKind.UP:
                cart_y -= 1
            elif cart_type == CartKind.DOWN:
                cart_y += 1

            for c in carts:
                if c['location'] == (cart_x, cart_y):
                    print('Number of steps taken:', steps)
                    return cart_x, cart_y

            cart['location'] = (cart_x, cart_y)

            grid_loc_kind = TrackKind(grid[cart_y][cart_x])
            if grid_loc_kind == TrackKind.XR:
                if cart_dir == 0:
                    cart['direction'] = 1
                    cart['type'] = \
                        xr_directions[(xr_directions.index(cart_type) - 1) % 4]
                elif cart_dir == 1:
                    cart['direction'] = 2
                elif cart_dir == 2:
                    cart['direction'] = 0
                    cart['type'] = \
                        xr_directions[(xr_directions.index(cart_type) + 1) % 4]
            else:
                cart['type'] = types[grid_loc_kind][cart_type]

        steps += 1


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


if __name__ == '__main__':
    # Tests
    TEST_CARTS, TEST_GRID = _create_state('./example-in.txt')
    assert(TEST_CARTS == [
        {'location': (2, 0), 'type': CartKind.RIGHT, 'direction': 0},
        {'location': (9, 3), 'type': CartKind.DOWN, 'direction': 0}
    ])
    assert(_tick(TEST_CARTS, TEST_GRID) == (7, 3))
    print('All tests passed!')

    # Solution
    CARTS, GRID = _create_state('./day13-input.txt')
    print(_tick(CARTS, GRID))
