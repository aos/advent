# Day 6 - Puzzle 1
# What is the size of the largest area?


import collections


def largest_area(inp_arr):
    areas = collections.defaultdict(int)
    max_x, max_y = _grid_size(inp_arr)
    grid = _generate_grid(max_x, max_y)
    populated = _populate_grid(inp_arr, grid, max_x, max_y)

    for y, row in enumerate(populated):
        for x, cell in enumerate(row):
            if len(cell) == 1:
                areas[cell[0]] += 1

    borders = {}
    for y, row in enumerate(populated):
        for x, cell in enumerate(row):
            if len(cell) == 1:
                if x == 0 or y == 0 or x == max_x or y == max_y:
                    borders[cell[0]] = True

    return max({k: areas[k] for k in (set(areas) - set(borders))}.values())


def _populate_grid(inp_arr, grid, max_x, max_y):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            # Calculate manhattan distance for each cell to the input_array
            # And use the one with the minimum distance
            min_point = None
            m = 1e9
            for point in inp_arr:
                d = _d_manh((x, y), point)
                if d < m:
                    m = d
                    min_point = point
                    grid[y][x] = [min_point]
                elif d == m:
                    grid[y][x].append(point)

    return grid


def _generate_grid(x, y):
    return [[[] for i in range(x + 1)] for i in range(y + 1)]


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
assert(largest_area(test_input) == 17)
print('All tests passed!')

with open('./day06-input.txt') as f:
    a = [tuple(int(i)
               for i in line.strip().split(','))
         for line in f]
    print(largest_area(a))
