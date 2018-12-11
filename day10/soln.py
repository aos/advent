# Day 10 - Puzzle 1 & 2
# What message will eventually appear in the sky?


import re
import time


# Using matplotlib
def plotted(inp_arr):
    import matplotlib.pyplot as plt
    import matplotlib.animation

    positions = []
    velocities = []
    steps = 0

    for i in inp_arr:
        pos, vel = _parse(i)
        positions.append(pos)
        velocities.append(vel)

    fig, ax = plt.subplots()
    xs, ys = list(zip(*positions))

    while steps < 10850:
        vel_xs, vel_ys = zip(*velocities)
        xs = list(map(sum, zip(xs, vel_xs)))
        ys = list(map(sum, zip(ys, vel_ys)))
        steps += 1

    sc = ax.scatter(xs, ys)

    def animate(i):
        nonlocal xs
        nonlocal ys
        nonlocal steps
        steps += 1

        print(steps)

        vel_xs, vel_ys = zip(*velocities)
        xs = list(map(sum, zip(xs, vel_xs)))
        ys = list(map(sum, zip(ys, vel_ys)))
        ax.clear()
        ax.scatter(xs, ys)

    ani = matplotlib.animation.FuncAnimation(fig, animate,
                                             interval=1000,
                                             repeat=True)
    plt.show()


def test_stars(inp_arr):
    import pprint
    pp = pprint.PrettyPrinter(width=160, compact=True)

    positions = []
    velocities = []
    steps = 0
    borders = None
    translate_x = None
    translate_y = None

    for i in inp_arr:
        pos, vel = _parse(i)
        positions.append(pos)
        velocities.append(vel)

    borders = _find_borders(positions)
    translate_x = abs(borders['min_x'])
    translate_y = abs(borders['min_y'])
    mp = _initialize_map(borders)

    while True:
        steps += 1
        print('step:', steps)
        for index, coords in enumerate(velocities):
            x, y = positions[index]
            mp[y + translate_y][x + translate_x] = '#'
            vel_x, vel_y = coords
            positions[index] = (x + vel_x, y + vel_y)

        time.sleep(1)
        pp.pprint(mp)
        mp = _initialize_map(borders)

    return mp


def _initialize_map(borders):
    return [
        [' ' for i in range(abs(borders['min_x']) + borders['max_x'] + 1)]
        for j in range(abs(borders['min_y']) + borders['max_y'] + 1)
    ]


def _find_borders(positions):
    max_x = -1e10
    max_y = -1e10
    min_y = 1e10
    min_x = 1e10

    for x, y in positions:
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x

        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y

    return {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y
    }


def _parse(string):
    return [tuple(map(int, j.split(',')))
            for j in [i.replace(' ', '')
                      for i in re.search(
                          r'position=<(.*)>\svelocity=<(.*)>', string
                      ).groups()]]


with open('./day10-input.txt') as f:
    a = [line.strip() for line in f]
    plotted(a)


test_simple = 'position=< 3, -2> velocity=<-1,  1>'
assert(_parse(test_simple) == [(3, -2), (-1, 1)])
print('All tests passed!')
