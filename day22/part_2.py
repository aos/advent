# Day 22 - Part 2
# What is the fewest # of minutes you can take to reach the target?


from heapq import heappush, heappop
from part_1 import cave_system


def a_star(start, end):
    h = []
    cost = {}
    pred = {}
    cost[start] = 0
    pred[start] = None

    heappush(h, 0)

    while len(h) > 0:
        current = heappop(h)
        nbs = neighbors(current)

        for nxt in nbs:
            pass


def neighbors(current, max_x, max_y):
    U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)
    return list(filter(lambda p: (
            p[0] >= 0 and
            p[0] <= max_x and
            p[1] >= 0 and
            p[1] <= max_y),
            [tuple(sum(a) for a in zip(current, d)) for d in (U, D, L, R)]))


s = (1, 1)
print(neighbors(s, 3, 3))
