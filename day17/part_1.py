# Day 17 - Puzzle 1
# How many tiles can the water reach within the range of 'y' values in scan?

import re
from pprint import pprint


class Model:
    def __init__(self, file):
        with open(file) as f:
            self.clay = [self.parse_clay(l.strip()) for l in f.readlines()]
        self.bounds = self.bound_box()
        self.earth = self.create_earth()

    def parse_clay(self, line):
        coord_one, co_val, coord_two, ct_min, ct_max = re.search(
            r'([xy]+)=(\d+),\s([xy]+)=(\d+)..(\d+)', line
        ).groups()

        return {
            coord_one: int(co_val),
            coord_two: range(int(ct_min), int(ct_max) + 1)
        }

    def bound_box(self):
        min_x = min_y = float('inf')
        max_x = max_y = -float('inf')

        for inp in self.clay:
            coord_one, coord_two = inp.items()
            if coord_one[0] == 'x':
                min_x = min(min_x, coord_one[1])
                max_x = max(max_x, coord_one[1])
            elif coord_one[0] == 'y':
                min_y = min(min_y, coord_one[1])
                max_y = max(max_y, coord_one[1])

            if coord_two[0] == 'x':
                min_x = min(min_x, coord_two[1][0])
                max_x = max(max_x, coord_two[1][-1])
            elif coord_two[0] == 'y':
                min_y = min(min_y, coord_two[1][0])
                max_y = max(max_y, coord_two[1][-1])

        return [(min_x - 1, min_y), (max_x + 1, max_y)]

    def create_earth(self):
        top_left, btm_right = self.bounds
        end_x = btm_right[0] - top_left[0]
        earth = [['.' for i in range(end_x + 1)]
                 for j in range(btm_right[1] + 1)]

        for vein in self.clay:
            coord_one, coord_two = vein.items()
            if coord_one[0] == 'x':
                for y in coord_two[1]:
                    x = coord_one[1] - top_left[0]
                    earth[y][x] = '#'
            elif coord_one[0] == 'y':
                for x in coord_two[1]:
                    x = x - top_left[0]
                    earth[coord_one[1]][x] = '#'

        return earth

    def fall(self, spring_x):
        # Get the transposed starting x position for spring
        spring_x = spring_x - self.bounds[0][0]
        water = (spring_x, 0)
        rnd = 0

        while rnd < 6:
            water = tuple(sum(item) for item in zip(water, (0, 1)))
            water_x, water_y = water
            self.earth[water_y][water_x] = '|'
            rnd += 1

    def scan(self):
        pass


# Tests
simple_model = Model('./simple-input.txt')
assert simple_model.clay == [
    {'x': 495, 'y': range(2, 8)},
    {'y': 7, 'x': range(495, 502)}
]
assert simple_model.bounds == [(494, 2), (502, 7)]
print('All tests passed!')

example_model = Model('./example-input.txt')
example_model.fall(500)
pprint(example_model.earth)
