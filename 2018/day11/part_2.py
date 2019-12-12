# Day 11 - Puzzle 2
# What is the X,Y,size identifier of the square with the largest total power?

from part_1 import (
    PUZZLE_INPUT,
    _find_level,
    _create_grid,
    _create_sum_grid,
    _calc_sub_matrix
)

WIDTH, HEIGHT = 300, 300
MAX_K = 300


# The brute force solution
def brute(sn, k):
    grid = _create_grid(WIDTH, HEIGHT)
    sum_grid = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            grid[y][x] = _find_level(x+1, y+1, sn)

    sum_grid = _create_sum_grid(grid)

    br_x, br_y, max_sum = _calc_sub_matrix(sum_grid, k)
    tl_x = br_x - k + 1
    tl_y = br_y - k + 1
    return tl_x + 1, tl_y + 1, max_sum


# Test
TEST_GRIDS = {
    18: (90, 269, 16),
    42: (232, 251, 12)
}
for sn, coords in TEST_GRIDS.items():
    local_k = 1
    local_max = -1e10
    local_x = local_y = 0

    for i in range(1, MAX_K + 1):
        x, y, this_max = brute(sn, i)

        if this_max > local_max:
            local_max = this_max
            local_k = i
            local_x = x
            local_y = y

    assert(TEST_GRIDS[sn] == (local_x, local_y, local_k))
print('All tests passed!')

# Solution
soln_k = 1
soln_max = -1e10
soln_x = soln_y = 0
for i in range(1, MAX_K + 1):
    x, y, this_max = brute(PUZZLE_INPUT, i)

    if this_max > soln_max:
        soln_max = this_max
        soln_k = i
        soln_x = x
        soln_y = y
print(soln_x, soln_y, soln_k)
