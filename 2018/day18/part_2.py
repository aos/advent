# Day 18 - Puzzle 2
# Total resource value after 1000000000 minutes?

from part_1 import Model
from itertools import count


def step(self):
    model_copy = [row[:] for row in self.model]
    for y, row in enumerate(model_copy):
        for x, cell in enumerate(row):
            # Get adjacents, apply rules
            adj = self.adjacents(x, y)
            self.apply_rule(x, y, cell, adj, model_copy)

    self.model = model_copy
    return self.model


Model.step = step

m = Model('./day18-input.txt')
seen = {}
prev = 0
for i in count(1):
    m.step()
    total = m.count()
    cycle = i - seen.get(total, 0)

    if cycle == prev:
        if 1_000_000_000 % cycle == i % cycle:
            print(total)
            break
    seen[total] = i
    prev = cycle
