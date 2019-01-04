# Day 22 - Part 1
# What is the total risk level for the smallest rectangle that includes the
# start and the target's coordinates


def regions(target, depth):
    risk = 0
    end_x, end_y = target
    grid = [[0 for i in range(end_x + 1)] for i in range(end_y + 1)]

    # Populate (x, 0) erosion
    for x in range(end_x + 1):
        grid[0][x] = erosion_level((x, 0), grid, target, depth)

    # Populate (0, y) erosion
    for y in range(end_y + 1):
        grid[y][0] = erosion_level((0, y), grid, target, depth)

    # Populate rest of grid erosion
    for gy, row in enumerate(grid):
        for gx, cell in enumerate(row):
            grid[gy][gx] = erosion_level((gx, gy), grid, target, depth)

    # Apply region type
    for ty, row in enumerate(grid):
        for tx, cell in enumerate(row):
            cell_risk = cell % 3
            grid[ty][tx] = cell_risk
            risk += cell_risk

    return risk, grid


def erosion_level(coords, grid, target, depth):
    x, y = coords
    tar_x, tar_y = target
    geo = 0

    if (
        (x == 0 and y == 0) or
        (x == tar_x and y == tar_y)
    ):
        geo = depth

    elif y == 0:
        geo = (x * 16807) + depth

    elif x == 0:
        geo = (y * 48271) + depth

    else:
        geo = (grid[y][x - 1] * grid[y - 1][x]) + depth

    return geo % 20183


if __name__ == '__main__':
    # Tests
    test_depth = 510
    test_target = (10, 10)
    assert regions(test_target, test_depth)[0] == 114
    print('All tests passed!')

    # Solution
    with open('./day22-input.txt') as f:
        depth, target = [line.rstrip().split(': ')[1]
                         for line in f.readlines()]
        target = [int(c) for c in target.split(',')]
        print(regions(target, int(depth))[0])
