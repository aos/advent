# Day 25 - UnionFind


from unionfind import UnionFind
from soln import parse_input


def man_d(p1, p2):
    return abs(p1[0] - p2[0]) \
        + abs(p1[1] - p2[1]) \
        + abs(p1[2] - p2[2]) \
        + abs(p1[3] - p2[3])


# Tests
p1 = (0, 0, 0, 0)
p2 = (3, 0, 0, 0)
assert man_d(p1, p2) == 3

cluster_size = [None, 2, 4, 3, 8]
for i in range(1, 5):
    test_points = parse_input(f'./example{i}-input.txt')
    uf = UnionFind(test_points)

    for p1 in test_points:
        for p2 in test_points:
            if (
                p1 is not p2 and
                man_d(p1, p2) <= 3
            ):
                uf.union(p1, p2)

    assert uf.num_sets == cluster_size[i]

print('All tests passed!')

# Solution
soln_pts = parse_input('./day25-input.txt')
uf_soln = UnionFind(soln_pts)

for pts1 in soln_pts:
    for pts2 in soln_pts:
        if (
            pts1 is not pts2 and
            man_d(pts1, pts2) <= 3
        ):
            uf_soln.union(pts1, pts2)

print(uf_soln.num_sets)
