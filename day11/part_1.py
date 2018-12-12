# Day 11 - Puzzle 1
# What is the <X,Y> coordinate of the top-left fuel cell of the 3x3 square with
# the largest total power?

# Note: Great infographic on finding the maximum submatrix here:
# https://www.techiedelight.com/calculate-sum-elements-sub-matrix-constant-time

WIDTH, HEIGHT = 300, 300
K = 3


def charge(sn):
    grid = _create_grid(WIDTH, HEIGHT)
    sum_grid = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            grid[y][x] = _find_level(x+1, y+1, sn)

    sum_grid = _create_sum_grid(grid)

    br_x, br_y = _calc_sub_matrix(sum_grid, K)
    tl_x = br_x - K + 1
    tl_y = br_y - K + 1
    return tl_x + 1, tl_y + 1


def _calc_sub_matrix(sum_grid, k):
    max_sum = -1e10
    xs = ys = 0

    for y in range(k - 1, len(sum_grid)):
        for x in range(k - 1, len(sum_grid)):
            total = sum_grid[y][x]

            # Check for out-of-bounds
            if y - k >= 0:
                total -= sum_grid[y - k][x]
            if x - k >= 0:
                total -= sum_grid[y][x - k]
            if (y - k >= 0) and (x - k >= 0):
                total += sum_grid[y - k][x - k]

            if total > max_sum:
                max_sum = total
                xs = x
                ys = y

    # Return bottom-right coordinates
    return xs, ys


def _create_sum_grid(grid):
    sum_grid = _create_grid(WIDTH, HEIGHT)

    # Initialize
    sum_grid[0][0] = grid[0][0]

    # Pre-process first row
    for y in range(1, len(sum_grid)):
        for x in range(1, len(sum_grid)):
            sum_grid[0][x] = grid[0][x] + sum_grid[0][x - 1]

    # Pre-process first column
    for y in range(1, len(sum_grid)):
        for x in range(1, len(sum_grid)):
            sum_grid[y][0] = grid[y][0] + sum_grid[y - 1][0]

    # Process rest of matrix
    for y in range(1, len(sum_grid)):
        for x in range(1, len(sum_grid)):
            sum_grid[y][x] = grid[y][x] \
                            + sum_grid[y - 1][x] \
                            + sum_grid[y][x - 1] \
                            - sum_grid[y - 1][x - 1]

    return sum_grid


def _create_grid(w, h):
    return [[0 for i in range(w)] for j in range(h)]


# Make sure to add one to the x and y values since we zero-index the grid
def _find_level(x, y, sn):
    rack_id = x + 10
    power = ((rack_id * y) + sn) * rack_id
    return ((power // 100) % 10) - 5


# Tests
TEST_POWER_LEVELS = {
    (3, 5, 8): 4,
    (122, 79, 57): -5,
    (217, 196, 39): 0,
    (101, 153, 71): 4
}
for k, v in TEST_POWER_LEVELS.items():
    assert(_find_level(*k) == v)

TEST_GRIDS = {
    18: (33, 45),
    42: (21, 61)
}
for k, v in TEST_GRIDS.items():
    assert(charge(k) == v)
print('All tests passed!')

# Solution
PUZZLE_INPUT = 2187
print(charge(PUZZLE_INPUT))
