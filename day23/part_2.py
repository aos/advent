# Day 23 - Part 2
# What is the shortest manhattan distance between any of those points and
# 0,0,0?


from part_1 import manh_d, parse_input


def solve(file):
    totals = []
    inp = parse_input(file)

    for x, y, z, r in inp:
        s = x + y + z
        totals.append((s - r, s + r))

    return totals


print(solve('./example2.txt'))
