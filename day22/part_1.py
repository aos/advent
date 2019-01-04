# Day 22 - Part 1
# What is the total risk level for the smallest rectangle that includes the
# start and the target's coordinates


def cave_system(target, depth, max_x, max_y):
    risk = 0
    grid = [[0 for i in range(max_x + 1)] for i in range(max_y + 1)]

    # Populate grid erosion
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
    max_x, max_y = test_target
    assert cave_system(test_target, test_depth, max_x, max_y)[0] == 114
    print('All tests passed!')

    # Solution
    with open('./day22-input.txt') as f:
        depth, target = [line.rstrip().split(': ')[1]
                         for line in f.readlines()]
        target = [int(c) for c in target.split(',')]
        print(cave_system(target, int(depth), target[0], target[1])[0])
