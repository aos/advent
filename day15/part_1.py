# Day 15 - Puzzle 1
# Find number of full rounds completed
# Find sum of hitpoints of all remaining units
# Outcome = rounds * sum_hp

# Notes:
# Calculate manhattan distance to target
# Phases:
# 1. Move
#   - Consider squares in range (immediately adjacent to target) and reachable
#   - Picks one by reading order if tie
# 2. Attack
#   - Determine all targets that are in range (immediately adjacent)
#       - if none, end turn
#   - Picks target with fewest hit points -> deals damage equal to attack power


from pprint import pprint


class Unit:
    def __init__(self, u_type, x, y, hp=200, ap=3):
        self.u_type = u_type
        self.x = x
        self.y = y
        self.hp = hp
        self.ap = ap
        self.alive = True

    def __str__(self):
        return f'{self.u_type}'

    def __repr__(self):
        return f'Unit({self.u_type}, {self.x}, {self.y}, {self.hp})'

    def step(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def find_targets(self, others):
        targets = []
        for t in others:
            if t is self:
                continue
            if t.u_type != self.u_type and t.alive:
                targets.append(t)

        return targets

    def adjacent_squares(self, m):
        adjacent = []
        U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)
        for d in (U, D, L, R):
            dir_x, dir_y = (sum(i) for i in zip((self.x, self.y), d))
            if (
                dir_x < 0 or
                dir_y < 0 or
                dir_x >= len(m[0]) or
                dir_y >= len(m)
            ):
                continue

            if m[dir_y][dir_x] == '.':
                adjacent.append((dir_x, dir_y))

        return adjacent


class Map:
    def __init__(self, file):
        self.units = []
        self.map = []

        with open(file) as f:
            for y, line in enumerate(f):
                line = line.strip()
                self.map.append([None] * len(line))
                for x, c in enumerate(line):
                    if c in 'EG':
                        u = Unit(c, x, y)
                        self.units.append(u)
                        self.map[y][x] = u
                    elif c == '#':
                        self.map[y][x] = '#'
                    else:
                        self.map[y][x] = '.'

    def print(self):
        print('\n'.join(''.join(str(x) for x in row) for row in self.map))

    def rounds(self, rounds):
        rnd = 0

        while rnd < rounds:
            self.units = self._sort_pts(self.units, key=lambda u: (u.y, u.x))

            for u in self.units:
                nearest = []
                targets = u.find_targets(self.units)

                for t in targets:
                    adj_sqs = t.adjacent_squares(self.map)
                    nearest.extend(self._sort_pts(
                        self._find_nearest(u, adj_sqs)
                    ))

                # Take step towards nearest chosen square
                #breakpoint()
                if len(nearest) > 0:
                    sq = nearest[0]
                    first = self._valid_dirs((u.x, u.y), sq)[0]
                    step_x, step_y = self._add_pts(first, (u.x, u.y))
                    self.map[u.y][u.x] = '.'
                    u.step(step_x, step_y)
                    self.map[step_y][step_x] = u

            rnd += 1

    def _find_nearest(self, unit, adjacents):
        reachable = []
        min_distance = 1e10
        for square in adjacents:
            if self._reach((unit.x, unit.y), square):
                dist = self._m_dist(square, (unit.x, unit.y))
                if dist <= min_distance:
                    min_distance = dist
                    reachable.append(square)

        return [s for s in reachable
                if self._m_dist((unit.x, unit.y), s) <= min_distance]

    def _reach(self, start, end):
        if start == end:
            return True

        valid_dirs = self._valid_dirs(start, end)
        for i in valid_dirs:
            new_x, new_y = self._add_pts(start, i)
            if (
                new_x < 0 and
                new_y < 0 and
                new_x >= len(self.map[0]) and
                new_y >= len(self.map)
            ):
                continue

            if self.map[new_y][new_x] == '.':
                return self._reach((new_x, new_y), end)

        return False

    def _valid_dirs(self, start, end):
        U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)
        valid_dirs = []
        start_x, start_y = start
        end_x, end_y = end
        diff_x = end_x - start_x
        diff_y = end_y - start_y

        if diff_x < 0:
            valid_dirs.append(L)
        elif diff_x > 0:
            valid_dirs.append(R)

        if diff_y < 0:
            valid_dirs.append(U)
        elif diff_y > 0:
            valid_dirs.append(D)

        return valid_dirs

    def _m_dist(self, p_1, p_2):
        x_1, y_1 = p_1
        x_2, y_2 = p_2
        return abs(x_1 - x_2) + abs(y_1 - y_2)

    def _sort_pts(self, pts, key=lambda pt: (pt[1], pt[0])):
        return sorted(pts, key=key)

    def _add_pts(self, pt1, pt2):
        return (sum(item) for item in zip(pt1, pt2))


m = Map('./example-move.txt')
m.print()
m.rounds(1)
print()
m.print()
