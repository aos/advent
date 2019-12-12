# Day 17
# Part 1 - How many tiles can water reach within range of 'y' values in scan?
# Part 2 - How much stale water is left?

import re
import sys
sys.setrecursionlimit(5000)


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
        self.fill(spring_x, 0)

    def fill(self, x, y):
        if y >= len(self.earth):
            return False

        self.earth[y][x] = '|'

        try:
            if self.earth[y + 1][x] == '.':
                self.fill(x, y + 1)

            if (
                self.earth[y + 1][x] in ['#', '~'] and
                self.earth[y][x + 1] == '.'
            ):
                self.fill(x + 1, y)
            if (
                self.earth[y + 1][x] in ['#', '~'] and
                self.earth[y][x - 1] == '.'
            ):
                self.fill(x - 1, y)

            if self.has_both_walls(x, y):
                self.fill_level(x, y)

        except IndexError:
            return False

    def has_both_walls(self, x, y):
        return self.has_wall(x, y, 1) and self.has_wall(x, y, -1)

    def has_wall(self, x, y, offset):
        curr = x
        if curr >= len(self.earth[0]) or curr < 0:
            return False
        while True:
            if self.earth[y][curr] == '.':
                return False
            if self.earth[y][curr] == '#':
                return True
            curr += offset

    def fill_level(self, x, y):
        return self.fill_side(x, y, 1), self.fill_side(x, y, -1)

    def fill_side(self, x, y, offset):
        curr = x
        if curr >= len(self.earth[0]) or curr < 0:
            return False
        while True:
            if self.earth[y][curr] == '#':
                return True
            self.earth[y][curr] = '~'
            curr += offset

    def count_water(self, types):
        total = 0
        min_y = self.bounds[0][1] if len(types) > 1 else 0
        for row in self.earth:
            for cell in row:
                if cell in types:
                    total += 1

        return total - min_y


# Tests
simple_model = Model('./simple-input.txt')
assert simple_model.clay == [
    {'x': 495, 'y': range(2, 8)},
    {'y': 7, 'x': range(495, 502)}
]
assert simple_model.bounds == [(494, 2), (502, 7)]

example_model = Model('./example-input.txt')
example_model.fall(500)
assert example_model.count_water(['~', '|']) == 57
assert example_model.count_water(['~']) == 29
print('All tests passed!')

# Solution Part 1
soln_model = Model('./day17-input.txt')
soln_model.fall(500)
print(soln_model.count_water(['~', '|']))

# Solution Part 2
print(soln_model.count_water(['~']))
