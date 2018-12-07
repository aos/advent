# Day 6 - Puzzle 1
# What is the size of the largest area?


import collections


def largest_area(inp_arr):
    areas = collections.defaultdict(int)
    max_x, max_y = _grid_size(inp_arr)
    grid = _generate_grid(max_x, max_y)
    pass


def _add_points(grid, inp):
    for x, y in inp:
        grid[y][x] = (x, y)

    return grid


def _generate_grid(x, y):
    return [[None for i in range(x + 1)] for i in range(y + 1)]


def _grid_size(inp):
    max_x = 0
    max_y = 0

    for x, y in inp:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return max_x, max_y


def _d_manh(p_1, p_2):
    """
    Calculates the manhattan distance between 2 points
    Args:
        p_1 (tuple[int]): The first point
        p_2 (tuple[int]): The second point

    Returns:
        int: The sum of taking the absolute value of
                p_1_x - p_2_x and p_1_y - p_2_y
    """
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    return abs(x_1 - x_2) + abs(y_1 - y_2)


# Tests
test_input = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9)
]
assert(_d_manh(test_input[0], test_input[1]) == 5)
assert(_grid_size(test_input) == (8, 9))
import pprint
pp = pprint.PrettyPrinter()
pp.pprint(_add_points(_generate_grid(*_grid_size(test_input)), test_input))
#assert(determine(test_input == 17))
print('All tests passed!')
