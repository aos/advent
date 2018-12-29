# Day 18 - Puzzle 1
# What is the total resource value after 10 mintues? (trees * lumberyards)


class Model:
    # Rules:
    # '.' -> '|' if 3 or more adjacent '|'
    # '|' -> '#' if 3 or more adjacent '#'
    # '#' -> '.' if not 1 adjacent '#' and 1 adjacent '|'
    def __init__(self, file):
        self.model = [list(line.strip()) for line in open(file).readlines()]
        self.max_x = len(self.model[0])
        self.max_y = len(self.model)

    def round(self, max_time):
        time = 0
        while time < max_time:
            model_copy = [row[:] for row in self.model]
            for y, row in enumerate(model_copy):
                for x, cell in enumerate(row):
                    # Get adjacents, apply rules
                    adj = self.adjacents(x, y)
                    self.apply_rule(x, y, cell, adj, model_copy)

            time += 1
            self.model = model_copy

        return self.model

    def adjacents(self, x, y):
        N, NE, E, SE, S, SW, W, NW = [(0, -1), (1, -1), (1, 0), (1, 1),
                                      (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        adj = []

        if x == 0:
            if y == 0:
                adj.extend([E, SE, S])
            elif y == self.max_y - 1:
                adj.extend([N, NE, E])
            elif y < self.max_y:
                adj.extend([N, NE, E, SE, S])

        elif x == self.max_x - 1:
            if y == 0:
                adj.extend([S, SW, W])
            elif y == self.max_y - 1:
                adj.extend([W, NW, N])
            elif y < self.max_y:
                adj.extend([S, SW, W, NW, N])

        elif x < self.max_x:
            if y == 0:
                adj.extend([E, SE, S, SW, W])
            elif y == self.max_y - 1:
                adj.extend([W, NW, N, NE, E])
            elif y < self.max_y:
                adj.extend([N, NE, E, SE, S, SW, W, NW])

        items = []
        for pt in adj:
            new_x, new_y = tuple(sum(item) for item in zip((x, y), pt))
            items.append(self.model[new_y][new_x])

        return items

    def apply_rule(self, x, y, curr, adjacents, copy):
        if curr == '.' and adjacents.count('|') >= 3:
            copy[y][x] = '|'

        elif curr == '|' and adjacents.count('#') >= 3:
            copy[y][x] = '#'

        elif curr == '#':
            yard_count = adjacents.count('#')
            tree_count = adjacents.count('|')

            if yard_count < 1 or tree_count < 1:
                copy[y][x] = '.'

        return True

    def print(self):
        print('\n'.join(''.join(cell for cell in row) for row in self.model))

    def count(self):
        trees = 0
        yards = 0
        for row in self.model:
            for cell in row:
                if cell == '|':
                    trees += 1
                if cell == '#':
                    yards += 1

        return trees * yards


if __name__ == '__main__':
    test_model = Model('./example-input.txt')
    test_model.round(10)
    assert test_model.count() == 1147
    print('All tests passed!')

    # Solution
    soln_model = Model('./day18-input.txt')
    soln_model.round(10)
    print(soln_model.count())
