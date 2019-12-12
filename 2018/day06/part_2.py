# Day 6 - Puzzle 2
# What is the size of the region containg all locations which have a total
# distance to all given coordinates less than 10000?


from part_1 import _d_manh, _grid_size, _generate_grid, TEST_INPUT


def find_size(input_arr, total_distance):
    size = 0
    max_x, max_y = _grid_size(input_arr)
    grid = _generate_grid(max_x, max_y)
    populated = _populate_grid(input_arr, grid, total_distance)

    for row in populated:
        for cell in row:
            if cell:
                size += 1

    return size


def _populate_grid(input_arr, grid, total_distance):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            coord = (x, y)
            s = sum([_d_manh(coord, point) for point in input_arr])

            if s < total_distance:
                grid[y][x].append(True)

    return grid


# Tests
assert(find_size(TEST_INPUT, 32) == 16)
print('All tests passed!')

with open('./day06-input.txt') as f:
    a = [tuple(int(i) for i in line.strip().split(',')) for line in f]
    print(find_size(a, 10000))
